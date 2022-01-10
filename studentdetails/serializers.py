
#from crudoperation.studentdetails.views import profiles
#from django.db.models import fields
from rest_framework import serializers
from studentdetails.models import Student
#from .model import profile

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','Firstname','Lastname','Course','Email','College','Year']


# class profileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = profile
#         fields="__all__"