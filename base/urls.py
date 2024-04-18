from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pay_slip/<int:pk>/', views.pay_slip, name="pay_slip")
]
