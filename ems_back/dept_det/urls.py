from django.urls import path
from . import views

urlpatterns = [
    path('man_all/', views.man_all),
    path('man_promote/<int:emp_id>/', views.man_promote),
    path('man_demote/<int:emp_id>/', views.man_demote),
]