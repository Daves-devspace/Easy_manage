import os
import uuid
from django.db import models
from apps.accounts.models import ClassTermFee
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


def generate_unique_name(instance,filename):
    name = uuid.uuid4()
    full_file_name=f"{name}-{filename}"
    return os.path.join(" student_images",full_file_name)

class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=30)
    father_id = models.IntegerField()
    father_mobile = PhoneNumberField(region="KE",blank=True, null=True)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=30)
    mother_id = models.IntegerField()
    mother_mobile = PhoneNumberField(region="KE",blank=True, null=True)
    address = models.TextField(20)
    

    def __str__(self) -> str:
        return f"{self.father_name} & {self.mother_name}"

    
    class Meta:
        db_table = 'parents'

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    grade = models.IntegerField()
    religion = models.CharField(max_length=100)
    joining_date = models.DateField()
    admission_number = models.CharField(max_length=15)
    section = models.CharField(max_length=10)
    student_image = models.ImageField(upload_to=generate_unique_name,blank=True, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="student")
    term_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def fee_balance(self):
        total_paid = self.fees.aggregate(total=models.Sum('amount_paid'))['total'] or 0
        balance = self.term_fee - total_paid
        return max(balance, 0)  # Ensure balance is never negative

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}  ({self.student_class})"
    
    def get_term_fee(self):
        try:
            class_term_fee = ClassTermFee.objects.get(grade=self.grade)
            return class_term_fee.term_fee
        except ClassTermFee.DoesNotExist:
            return None
    
    class Meta:
        db_table = 'students'
    
    
class Fee(models.Model):
    student = models.ForeignKey(Student, related_name='fees', on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    description = models.CharField(max_length=20,default=00)
    date = models.DateField()
    
    def __str__(self):
        return f"Fee Record for: {self.student.first_name} {self.student.last_name} on {self.date}"
    @property
    def remaining_balance(self):
        # Calculates the balance for this transaction
        return self.amount_due - self.amount_paid
    class Meta:
        db_table = 'fees'
        
        
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    subject = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return f"{self.title}-{self.isbn}"
    verbose_name = 'Book'
    verbose_name_plural = 'Books'
    ordering = ['isbn']
    db_table = 'books'
    
class Transaction(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='transactions')
    status = models.CharField(max_length=20)
    expected_return_date = models.DateField()
    return_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.book}-{self.student}"
    
    @property
    def total_fine(self):
        if self.return_date and self.expected_return_date and self.return_date> self.expected_return_date:
            amount = (self.return_date - self.expected_return_date).days * 10
            return amount
        return 0
    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ['-created_at']
        db_table = 'transactions'
        
class Payment(models.Model):
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE)
    merchant_request_id = models.CharField(max_length=100)
    checkout_request_id = models.CharField(max_length=100)
    code = models.CharField(max_length=30,null=True)
    amount = models.IntegerField()
    status = models.CharField(max_length=20,default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['-created_at']
        db_table = 'payments'
    
    def __str__(self):
        return f"{self.transaction}-{self.code} -{self.amount}"   

        
    
    
