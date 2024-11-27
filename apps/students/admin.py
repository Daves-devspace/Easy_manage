from django.contrib import admin
from .models import Parent, Student,Fee,Book,Transaction,Payment

# Register your models here.
admin.site.site_header ='Merryland Management System'
admin.site.site_title = 'Merryland Friends'
admin.site.register(Parent)
admin.site.register(Fee)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','grade','admission_number','gender']
    search_fields = ['first_name','grade','admission_number']
    list_per_page = 30
    
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','year','isbn','subject']
    search_fields = ['title','author','year','isbn','subject']
    list_per_page = 35
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['book','student','status','expected_return_date']
    search_fields = ['book','student','status','expected_return_date']
    list_per_page =  25
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction','code','status','amount','created_at']
    search_fields = ['transaction','code','status','amount','created_at']
    list_per_page = 25 
    
admin.site.register(Student,StudentAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Payment,PaymentAdmin)
        