from common.model import Model
from models.file import File

class Gallery(Model):
    table = 'gallery'

    def __init__(self, **kwargs):
        super(Gallery, self).__init__(**kwargs)

    def delete(self):
        if getattr(self, 'eid', None):
            for f in File().filter( gallery_eid = self.eid ):
                f.delete()
        super(Gallery, self).delete()
