from mongoengine import Document

class APIBaseModel(Document):
    """
    Base Model which only needs to be inherited.
    """
    meta = {
        'abstract': True
    }

    @classmethod
    def find(cls, key=None, value=None):
        if not key:
            return cls.objects
        return cls.objects(**{key: value})