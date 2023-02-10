from django.contrib import admin
from django.urls import path , include
from Student import views

urlpatterns = [
    path("" ,views.index , name="index"),
    path("class_view/<standard>" ,views.class_view ,name="class_view"),
    path("student_profile/<standard>/<rollno>" ,views.student_profile ,name="student_profile"),
    path("admi_form/<standard>" ,views.admi_form ,name="admi_form")
]