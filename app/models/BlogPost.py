import datetime
from models.Base import Base as BaseModel

class BlogPost(BaseModel):

    def __init__(self, ):
        self.id = blog_id
        self.status_id = status_id
        self.category_id = category_id
        self.published_at = published_at
        self.details = details
        self.created_at = created_at
        self.last_updated_at = last_updated_at

    def __repr__(self):
        return(
            u'BlogPost(id={}, status_id={}, category_id={}, published_at={}, details={})'
            .format(self.id, self.status_id, self.category_id, self.published_at,
                    self.details))




