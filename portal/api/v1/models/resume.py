from mongoengine import StringField, IntField, FloatField, ListField
from api_base_model import APIBaseModel

class Resume(APIBaseModel):
    """
    Model that defines the Resume.
    """
    studentid = StringField()
