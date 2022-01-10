from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
# from profiles.serializers import ProfileSerializer
# from rest_framework.response import Response

#Create your views here.

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student
    serializer_class = StudentSerializer

# class profiles(APIView):
#     def post(self,request):
#         serializer=profileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'done'})
#         return Response(serializer.errors)
#     def get(self,request):
#         data=profile.object.all()
#         serializer=profileSerializer(data, many=True)
#         return Response(serializer.data)