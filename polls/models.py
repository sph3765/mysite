from django.db import models
import datetime
from django.db import models 
from django.utils import timezone
# Create your models here.
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text


class Employee(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

    def __str__(self):
      return self.firstName + " " + self.lastName

class Department(models.Model):
    departmentName = models.CharField(max_length=200)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


    def __str__(self):
      return self.departmentName 


# class Company(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#       return self.name


# class Programmer(models.Model):
#   name = models.CharField(max_length=200)
#   company = models.ForeignKey(Company, on_delete=models.CASCADE) 
#   def __str__(self):
#     return self.name
