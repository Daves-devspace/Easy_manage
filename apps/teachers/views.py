from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TeacherForm,SubjectForm
from .models import Teacher


# Create your views here.
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Teacher added successfully.")
            return redirect('teachers')
        else:       
            return render(request,'teachers/add-teacher.html',{'form':form})
    form = TeacherForm()
    return render(request, 'teachers/add-teacher.html', {'form': form})

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request,'teachers/teachers.html',{'teachers':teachers})


def view_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher,id = teacher_id)
    return render(request,'teachers/view_teacher.html',{'teacher':teacher})


def edit_teacher(request,teacher_id):
    teacher = get_object_or_404(Teacher,id=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST,instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request,"Teacher updated successfully. ")
            return redirect('teacher_list')


    else:
        form = TeacherForm(instance=teacher)
    return render(request,'teachers/edit_teacher.html',{'form':form,'teacher':teacher})


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Subject added successfully.")
            return redirect('subjects')
        else:       
            return render(request,'teachers/add-subject.html',{'form':form})
    form = SubjectForm()
    return render(request, 'teachers/add-subject.html', {'form': form})

