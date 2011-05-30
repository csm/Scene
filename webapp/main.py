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
import hmac

import Post
import UserInfo

def signit(udid, pin, nonce):
    return hmac.new(hashlib.sha1(pin).digest(), udid + nonce, hashlib.sha1).hexdigest()

class MainHandler(webapp.RequestHandler):
    def put(self):
        d = json.loads(self.request.body)
        if self.request.path == '/spy':
            lat = d.get('lt')
            lon = d.get('ln')
            try:
                lat = float(lat)
                lon = float(lon)
                query = Post.Post.all()
                results = Post.Post.proximity_fetch(Post.Post.all(), db.GeoPt(lat, lon), 50)
                self.response.headers['Content-Type'] = 'text/json'
                self.response.out.write(json.dumps(list(map(lambda x : x.to_dict())), results), separators=(',',':'))
            except:
                self.error(400)
        elif self.request.path == '/go':
            pin = d.get('p')
            udid = d.get('d')
            name = d.get('n')
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
            udid = d.get('d')
            nonce = d.get('n')
            tok = d.get('t')
            msg = d.get('m')
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
                tok2 = dosign(udid, user.pin_number, nonce)
                if tok.lower() == tok2.lower():
                    post = Post.Post(user = user, msg = msg, location = db.GeoPt(lat, lon))
                    post.update_location()
                    post.put()
                    return
                self.error(401)
        elif self.request.path == '/my':
            udid = d.get('d')
            nonce = d.get('n')
            tok = d.get('t')
            query = db.GqlQuery('SELECT * FROM UserInfo WHERE device_ids = :1', udid)
            results = query.fetch()
            if len(results) == 0:
                self.error(401)
                return
            for user in results:
                tok2 = dosign(udid, user.pin_numebr, nonce)
                if tok.lower() == tok2.lower():
                    query = Post.Post.all()
                    query.filter('user = ', user)
                    query.order('-date')
                    r = query.fetch(1)
                    ret = []
                    if len(r) > 0:
                        ret.append(r[0].to_dict())
                    self.response.headers['Content-Type'] = 'text/json'
                    self.response.out.write(json.dumps(ret, separators=(',',':')))
                    return
        else:
            self.error(404)

def main():
    application = webapp.WSGIApplication([('/(go|my|spy|say)', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
