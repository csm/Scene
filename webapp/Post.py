# Post.py -- a post to scene.

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
        d['u'] = self.user.to_public_dict()
        d['d'] = self.date.strftime('%Y-%m-%d %H:%M:%S')
        d['m'] = self.msg
        d['l'] = [ self.location.lat, self.location.lon ]