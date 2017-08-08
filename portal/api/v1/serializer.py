from rest_framework import serializers
from api.v1.models.student import Student

class APIBaseSerializer(serializers.Serializer):
    def create(self, validated_data):
        obj = Student()
        for key in validated_data:
            try:
                getattr(obj, str(key))
                setattr(obj, str(key), validated_data[key])
            except:
                print "Failed to create."

        try:
            obj.save()
            return obj
        except:
            return None

    def update(self, instance, validated_data):
        for key in validated_data:
            try:
                setattr(instance, str(key), validated_data.get(key, getattr(instance, key)))
            except:
                continue
        try:
            instance.save()
            return instance
        except:
            return None

class StudentSerializer(APIBaseSerializer):
    _id = serializers.JSONField(read_only=True)
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    college_id = serializers.CharField(required=True)
    branch = serializers.CharField(required=True)
    contact_no = serializers.IntegerField(required=False)
    score = serializers.FloatField(required=True)
    resume = serializers.ListField(required=False)
    company_eligible_for = serializers.ListField(required=False)
    company_applied_for = serializers.ListField(required=False)

class CompanySerializer(APIBaseSerializer):
    _id = serializers.JSONField(read_only=True)
    name = serializers.CharField(required=True)
    location = serializers.CharField(required=False)
    description = serializers.CharField(required=True)

class ResumeSerializer(APIBaseSerializer):
    _id = serializers.JSONField(read_only=True)
    student_id = serializers.CharField(required=True)