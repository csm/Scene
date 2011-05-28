# UserInfo.py -- a user model.

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
    
    def to_public_dict(self):
        """
        Turn this UserInfo into a dict, suitable for serialization to the public.
        """
        d = {}
        d['n'] = self.name
        if self.avatar != None:
            d['a'] = str(self.avatar)