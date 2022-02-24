from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import include,url

urlpatterns=[
    path('order/',views.RazorPayOrder.as_view(), name = 'order'),
    path('checkout_verification/',views.PaymentDetailsView.as_view(),name='checkout_verification'),
]