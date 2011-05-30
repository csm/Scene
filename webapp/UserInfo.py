# UserInfo.py -- a user model.
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

from google.appenine.ext import db
from google.appenine.ext import blobstore

class UserInfo(db.Model):
    # A list of device IDs associated with this user.
    device_ids = db.StringListProperty()
    
    # An encoded BlobKey containing the user's avatar
    avatar = blobstore.BlobReferenceProperty()

    # The user's PIN number, in the range [0..99999999]
    pin_number = db.IntegerProperty(required = True)
    
    # The user's name.
    name = db.StringProperty(required = True)
