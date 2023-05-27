from django.urls import path

from attendance import views

urlpatterns = [
    path('<int:branch_id>/',views.StudentAttendanceView.as_view()),
    path('<int:branch_id>/detailed/',views.DetailedTodayAttendanceOverview.as_view()),
    path('<int:branch_id>/message/',views.SendMessage.as_view())
]
