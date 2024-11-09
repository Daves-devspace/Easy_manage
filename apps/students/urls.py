"""
URL configuration for manage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('add/', views.add_student, name='add_student'),
    path('students/add_fee/<int:student_id>', views.add_fee, name='add_fee'),
    path('students/students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('detail/<int:student_id>/',views.student_details,name='student_details'),    
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    
    path('library',views.books_in_store,name='books_in_store')


]
