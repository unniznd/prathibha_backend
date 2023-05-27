
from django.urls import path

from branch_class import views

urlpatterns = [
    path('',views.get_branch),
    path('<int:id>/',views.get_branch),
    path('create/',views.create_branch),
    path('update/<int:id>/',views.update_branch),
    path('delete/<int:id>/',views.delete_branch),

    path('class/',views.get_class_division),
    path('class/<int:id>/',views.get_class_division),
    path('class/create/',views.create_class_division),
    path('class/update/<int:id>/',views.update_class_division),
    path('class/delete/<int:id>/', views.delete_class_division),

    path('<int:branch_id>/class/', views.get_class_division_branch_wise)
]
