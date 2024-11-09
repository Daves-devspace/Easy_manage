# apps/teachers/forms.py
from django import forms
from .models import Teacher,Subject

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'subject','teacher_class', 'phone_number']
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']