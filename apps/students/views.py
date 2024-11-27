
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from decimal import Decimal
from django.db import transaction

from .forms import StudentForm,FeeForm
from apps.accounts.models import ClassTermFee
from .models import Student, Parent, Fee,Book


# Create your views here.
@login_required
def index(request):
    return render(request, 'home/index.html')

@login_required
@permission_required("manage.add_student",raise_exception=True)
@transaction.atomic
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student=form.save() #save the student object
            grade = form.cleaned_data['grade'] #access grade from the form
            joining_date = form.cleaned_data.get('joining_date')  # Fetch the joining date
            try:
                term_fee_object = ClassTermFee.objects.get(grade=grade)
                term_fee = term_fee_object.term_fee
            # This will handle both `Student` and `Parent` saving logic
                Fee.objects.create(
                    student=student,
                    amount_due=term_fee,
                    amount_paid=0,
                    date=joining_date
                )
                messages.success(request, f"Student {student.first_name} added and term fee of Ksh{term_fee} assigned.")
            except ClassTermFee.DoesNotExist:
                messages.error(request, "Term fee not found for this grade. Please add a term fee for the grade.")
            return redirect('students')  # Redirect to students list or another appropriate page
    else:
        form = StudentForm()  # Render an empty form for GET requests

    return render(request, 'students/add-student.html', {'form': form})
       
    
@login_required
def students(request):
    student_list = Student.objects.select_related('parent').all()
    
    paginator = Paginator(student_list,per_page=15)
    page_number = request.GET.get('page',1)
    try:
        paginated_data = paginator.page(page_number)
    except (PageNotAnInteger,EmptyPage):
        paginated_data = paginator.page(1)
    return render(request, "students/students.html",{"student_list":paginated_data})

@login_required
@permission_required("manage.change_student",raise_exception=True)
def edit_student(request,student_id):
    #retrieving the student object or return a 404 if not found
    student = get_object_or_404(Student,id=student_id)

    if request.method == 'POST':
        #create a form instance with post data and existing student instances
         form = StudentForm(request.POST,request.FILES,instance=student)
         if form.is_valid():
             form.save() #save change to db
             messages.success(request,"Student updated successfully")
             return redirect("students")
         else:
             messages.error(request,"Failed to update student.Please correct the errors.")
    else:
        #populate the form with the existing student data
         form = StudentForm(instance=student)
    return render(request, "students/edit-student.html", {'form':form, 'student':student})

@login_required
@permission_required("manage.delete_student",raise_exception=True)
def delete_student(request,student_id):
    student=Student.objects.get(id=student_id)
    student.delete()
    messages.info(request,f"Student {student.first_name} was deleted")
    return redirect('students')

@login_required
def add_fee(request,student_id):
    student = get_object_or_404(Student, id=student_id)
    #fetch latest bal
    latest_fee = Fee.objects.filter(student=student).order_by('-date').first()
    new_amount_due = latest_fee.remaining_balance if latest_fee else Decimal('0.00')
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            fee = form.save(commit=False)
            fee.student = student
            fee.amount_due = new_amount_due  # Set the new amount_due dynamically
            # Save the fee record to the database
            fee.save()

            # Add a success message
            messages.success(request, 'The fee has been successfully saved')
            # Redirect to the student detail page
            return redirect('student_details', student_id=student.id) 
        else:
            print(f"Form errors: {form.errors}") # Redirect to a view that lists the fees
    else:
        form = FeeForm(initial={'amount_due':new_amount_due})
          
    fees = Fee.objects.filter(student=student).order_by('-date')
    
    return render(request, 'students/fees.html', {'form': form,'student':student,'fees': fees})

       
       

@login_required
@permission_required("Students.view_student",raise_exception=True)
def student_details(request,student_id):
    student=Student.objects.get(id=student_id)
    term_fee = student.get_term_fee()
    fee_balance = student.fee_balance()
    return render(request,'students/student-details.html',{'student': student,'term_fee': term_fee,'fee_records': student.fees.all(),'fee_balance':fee_balance})
    

def books_in_store(request):
    books = Book.objects.all()
    return render(request,'library/books_in_store.html',{'books':books})





