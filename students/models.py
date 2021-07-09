from students_marks.settings import DATABASES
from django.db import models
from django.db.models.fields import FloatField,CharField,DateTimeField

# Create your models here.




class students(models.Model):
    name = models.CharField(max_length = 20)
    #Id = models.AutoField(primary_key=True,default=0)
    english = models.FloatField()
    tamil = models.FloatField()
    maths = models.FloatField()
    science = models.FloatField()
    social = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    