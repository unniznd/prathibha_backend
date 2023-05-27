from django.urls import path

from .views import FeeView, GenerateFee

urlpatterns = [
    path('<int:branchId>/', FeeView.as_view()),
    path('<int:branchId>/generate/', GenerateFee.as_view()),
]