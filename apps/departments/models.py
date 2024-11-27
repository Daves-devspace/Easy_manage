from django.db import models
from apps.teachers.models import Teacher

# Create your models here.



class Department(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_DEFAULT, default=None,related_name='teachers')
    number = models.IntegerField()
    
    def __str__(self):
        return f"{self.department.name} {self.department.teacher}"
