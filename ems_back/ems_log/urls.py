from django.urls import path
from . import views

urlpatterns = [
    path('cmp_login/', views.company_login),
    path('cmp_reg/', views.company_registration),
]