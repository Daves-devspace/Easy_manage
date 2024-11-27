from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher_class= models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    subject = models.ManyToManyField(Subject,related_name='teachers')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.teacher_class}"
