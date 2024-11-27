from django.db import models

# Create your models here.
class ClassTermFee(models.Model):
    grade = models.CharField(max_length=50, unique=True)  # e.g., Grade 1, Grade 2
    term_fee = models.DecimalField(max_digits=10, decimal_places=2)  # Term fee amount

    def __str__(self):
        return f"{self.grade} - ${self.term_fee}"
    
    
    