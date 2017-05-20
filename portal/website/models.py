# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import Document, StringField, IntField, FloatField, ListField


# Create your models here.

class Resume(Document):
    """
    Model that defines the Resume.
    """
    pass

class Student(Document):
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

class Company(Document):
    """
    Model that defines a company
    """
    pass