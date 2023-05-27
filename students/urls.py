from django.urls import path

from students import views

urlpatterns = [
    path('<int:branch_id>/',views.ViewStudents.as_view()),
]
