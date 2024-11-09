# forms.py
from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import Student,Parent,Fee


GENDER_CHOICES = {"Male":"Male","Female":"Female"}
RELIGION_CHOICES = {"Christian":"Christian","Muslim":"Muslim"}
class StudentForm(forms.ModelForm):
    
    father_name = forms.CharField(max_length=100, required=False)
    father_occupation = forms.CharField(max_length=20, required=False)
    father_id = forms.IntegerField( required=False)
    father_mobile = PhoneNumberField(region="KE", label="Father's Mobile Number")
    mother_name = forms.CharField(max_length=100, required=False)
    mother_occupation = forms.CharField(max_length=20, required=False)
    mother_id = forms.IntegerField( required=False)
    mother_mobile = PhoneNumberField(region="KE", label="Father's Mobile Number")
    address = forms.CharField(widget=forms.Textarea, required=False)
    
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect) #form.select
    religion = forms.ChoiceField(choices=RELIGION_CHOICES,widget=forms.Select)
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name',  'gender', 'date_of_birth',
            'grade', 'religion', 'joining_date',
            'admission_number', 'section', 'student_image',
            'father_name', 'father_occupation', 'father_id', 'father_mobile',
            'mother_name', 'mother_occupation', 'mother_id', 'mother_mobile',
            'address'
        ]
        widgets = {
            'date_of_birth':forms.DateInput(attrs={'class':'datepicker','type':'date'}),
            'joining_date':forms.DateInput(attrs={'class':'datepicker','type':'date'}),
        }
    def __init__(self, *args, **kwargs):
        # Initialize parent data into the form if the student has a parent
        super().__init__(*args, **kwargs)
        parent = getattr(self.instance, 'parent', None)
        if parent:
            self.fields['father_name'].initial = parent.father_name
            self.fields['father_occupation'].initial = parent.father_occupation
            self.fields['father_id'].initial = parent.father_id
            self.fields['father_mobile'].initial = parent.father_mobile
            self.fields['mother_name'].initial = parent.mother_name
            self.fields['mother_occupation'].initial = parent.mother_occupation
            self.fields['mother_id'].initial = parent.mother_id
            self.fields['mother_mobile'].initial = parent.mother_mobile
            self.fields['address'].initial = parent.address
            
    def save(self, commit=True):
        # Save parent details first
        parent_data = {
            'father_name': self.cleaned_data.get('father_name'),
            'father_occupation': self.cleaned_data.get('father_occupation'),
            'father_id': self.cleaned_data.get('father_id'),
            'father_mobile': self.cleaned_data.get('father_mobile'),
            'mother_name': self.cleaned_data.get('mother_name'),
            'mother_occupation': self.cleaned_data.get('mother_occupation'),
            'mother_id': self.cleaned_data.get('mother_id'),
            'mother_mobile': self.cleaned_data.get('mother_mobile'),
            'address': self.cleaned_data.get('address'),
            
        }

        if self.instance.pk and self.instance.parent:
            # Update existing parent
            for field, value in parent_data.items():
                setattr(self.instance.parent, field, value)
            self.instance.parent.save()
        else:
            # Create new parent
            parent = Parent.objects.create(**parent_data)
            self.instance.parent = parent

        return super().save(commit=commit)
            
            
            
class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['amount_due', 'amount_paid', 'date']  # Fields to include in the form
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            ## Makes sure the date field is rendered as a date input
        }

    # for add custom validation if needed
    def clean_amount_due(self):
        amount_due = self.cleaned_data.get('amount_due')
        if amount_due < 0:
            raise forms.ValidationError("Amount due cannot be negative")
        return amount_due

    def clean_amount_paid(self):
        amount_paid = self.cleaned_data.get('amount_paid')
        if amount_paid < 0:
            raise forms.ValidationError("Amount paid cannot be negative")
        return amount_paid
