from django.urls import  path
from . import views

urlpatterns=[
     path('subject',views.add_subject,name='add_subject'),
    path('add/',views.add_teacher,name='add_teacher'),
    path('teachers/',views.teachers,name='teachers'),

    path('teachers/<int:teacher_id>/',views.view_teacher,name='view_teacher'),
    path('teachers/<int:teacher_id>/edit/',views.edit_teacher,name='edit_teacher'),
]
