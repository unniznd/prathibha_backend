
from django.contrib import admin
from django.urls import path, include

from users.views import ObtainAuthTokenWithUserId, GetDashboardDetails
from attendance.views import HolidayView, TodayAttendanceOverview
from students.views import DashboardOverview

from .views import AttendanceReport, FeeReport


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', ObtainAuthTokenWithUserId.as_view()),
    path('dashboard/', GetDashboardDetails.as_view()),
    path('holiday/', HolidayView.as_view()),
    path('dashboard-overview/<int:branch_id>/', DashboardOverview.as_view()),
    path('today-attendance-overview/<int:branch_id>/', TodayAttendanceOverview.as_view()),
    path('attendance-report/<int:branchId>/', AttendanceReport.as_view()),
    path('fee-report/<int:branchId>/', FeeReport.as_view()),

    path('branch/', include('branch_class.urls')),
    path('students/', include('students.urls')),
    path('attendance/', include('attendance.urls')),
    path('fee/', include('fee.urls')),
]
