from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TermFeeForm
from django.contrib import messages
from .models import ClassTermFee

# Create your views here.
def test_view(request):
    return HttpResponse("Accoount view is working.")

def manage_term_fees(request):
    if request.method == 'POST':
        form = TermFeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Term fee for{form.cleaned_data['grade']} updated to Ksh{form.cleaned_data['term_fee']}.")
            return redirect('manage_term_fees')
        else:
            print(f"Form errors:{form.errors}")
            messages.error(request,"There was an error updating fee")
    else:
        form = TermFeeForm()
    term_fees = ClassTermFee.objects.all()
    return render(request, 'accounts/manage-term-fee.html', {'form':form,'term_fees':term_fees})

