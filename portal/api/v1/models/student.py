from mongoengine import StringField, IntField, FloatField, ListField

from api_base_model import APIBaseModel

class Student(APIBaseModel):
    """
    Model that defines the student.
    """
    name = StringField(required=True)
    email = StringField(required=True)
    college_id = StringField(required=True)
    branch = StringField(required=True)
    contact_no = IntField()

    # it can be percentage/CGPA
    score = FloatField(required=True)

    # object IDs of the resume are referenced
    resume = ListField()

    # object IDs of companies are referenced
    company_eligible_for = ListField()

    # this has the following structure : {'_id': <>, 'name': <>, 'status': <>}
    # status allows us to capture if the student is placed/in-progress
    company_applied_for = ListField()
