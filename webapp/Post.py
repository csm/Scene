# Post.py -- a post to scene.
#
# Copyright (C) 2011 Casey Marshall
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

from geo.geomodels import GeoModel

import UserInfo

class Post(GeoModel):
    # Who posted this.
    user = db.ReferenceProperty(UserInfo.UserInfo, required = True)
    
    # When this was posted.
    date = db.DateTimeProperty(required = True, auto_now_add = True)
    
    # The message.
    msg = db.StringProperty(required = True, multiline = True)
    
    def to_dict(self):
        """
        Turn this Post into a dict, suitable for serialization.
        """
        d = {}
        d['k'] = str(self.key())
        d['d'] = self.date.strftime('%Y-%m-%d %H:%M:%S')
        d['m'] = self.msg
        d['l'] = [ self.location.lat, self.location.lon ]
        d['n'] = self.user.name
        if self.user.avatar != None:
            d['a'] = self.user.avatar
        return d