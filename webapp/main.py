#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import util

import re
try:
    import json
except:
    from django.utils import simplejson as json

import hashlib

import Post
import UserInfo

class MainHandler(webapp.RequestHandler):
    def get(self):
        if self.request.path == '/spy':
            lat = self.request.get('lt')
            lon = self.request.get('ln')
            try:
                lat = float(lat)
                lon = float(lon)
                query = Post.Post.all()
                results = Post.Post.proximity_fetch(Post.Post.all(), db.GeoPt(lat, lon), 50)
                self.response.headers['Content-Type'] = 'text/json'
                self.response.out.write(json.dumps(list(map(lambda x : x.to_dict())), results), separators=(',',':'))
            except:
                self.error(400)
        else:
            self.error(404)

    def post(self):
        if self.request.path == '/enter':
            pin = self.request.get('p')
            udid = self.request.get('d')
            name = self.request.get('n')
            query = db.GqlQuery('SELECT * FROM UserInfo WHERE device_ids = :1', udid)
            results = query.fetch()
            for user in results:
                if user.pin_number == pin:
                    user.name = name
                    user.put()
                    return
            user = UserInfo.UserInfo(device_ids = [udid], pin_number = pin, name = name)
            user.put()
        elif self.request.path == '/say':
            udid = self.request.get('d')
            nonce = self.request.get('n')
            tok = self.request.get('t')
            msg = self.request.get('m')
            try:
                lat = float(self.request.get('lt'))
                lon = float(self.request.get('ln'))
            except:
                self.error(400)
                return
            if udid == None or nonce == None or tok == None or msg == None:
                self.error(400)
                return
            query = db.GqlQuery('SELECT * FROM UserInfo WHERE device_ids = :1', udid)
            results = query.fetch()
            if len(results) == 0:
                self.error(401)
                return
            for user in results:
                md = hashlib.sha1()
                md.update(udid)
                md.update(nonce)
                md.update(user.pin_number)
                tok2 = md.hexdigest()
                if tok.lower() == tok2.lower():
                    post = Post.Post(user = user, msg = msg, location = db.GeoPt(lat, lon))
                    post.update_location()
                    post.put()
                    return
                self.error(401)
        else:
            self.error(404)

def main():
    application = webapp.WSGIApplication([('/(enter|spy|say)', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
