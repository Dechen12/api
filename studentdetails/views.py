from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import  Response
from studentdetails.pagination import CustomPageNumberPagination
#Create your views here.



class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student
    serializer_class = StudentSerializer






# class StudentList(APIView):

#     def get(self,request):
#         stdobj= Student.objects.all()
#         stdsserializeobj= StudentSerializer(stdobj,many=True)
#         return Response(stdsserializeobj.data)