from django.db import models

# Create your models here.
class Student(models.Model):
    Firstname = models.CharField(max_length=100,blank=True )
    Lastname = models.CharField(max_length=100,blank=True )
    Course = models.CharField(max_length=100,blank=True )
    Email = models.CharField(max_length=100,blank=True )
    College = models.CharField(max_length=100,blank=True )
    Year = models.CharField(max_length=100,blank=True )

    def __str__(self):
        return self.Firstname

    def __str__(self):
        return self.Lastname

    def __str__(self):
        return self.Course

    def __str__(self):
        return self.Email

    def __str__(self):
        return self.College

    def __str__(self):
        return self.Year

class profile(models.Model):
    name=models.CharField(max_length=200)