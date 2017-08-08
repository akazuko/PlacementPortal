from mongoengine import StringField, IntField, FloatField, ListField

from api_base_model import APIBaseModel

class Company(APIBaseModel):
    """
    Model that defines a company
    """
    name = StringField(required=True)
    location = StringField(required=False)
    description = StringField(required=True)
