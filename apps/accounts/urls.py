from django.urls import path
from .import views

urlpatterns =[
    path('manage-fees',views.manage_term_fees,name='manage_term_fees'),
]