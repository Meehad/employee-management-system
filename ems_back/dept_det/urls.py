from django.urls import path
from . import views

urlpatterns = [
    path('dept_all/', views.dept_all),
    path('dept_add/', views.Dep_add),
    path('man_promote/<int:emp_id>/', views.man_promote),
    path('man_demote/<int:emp_id>/', views.man_demote),
    path('dept_delete/<int:dept_id>/', views.dept_delete),
]