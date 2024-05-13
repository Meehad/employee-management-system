from django.urls import path
from . import views

urlpatterns = [
    path('emp_post/', views.emp_add),
    path('emp_all/', views.emp_all),
    path('emp_delete/<int:emp_id>/', views.emp_delete),
]
