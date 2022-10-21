from django.urls import path

from .views import admin_dashboard, send_sms_view

urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'), 
    path('send-sms/', send_sms_view, name='send_sms')
]
