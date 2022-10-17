from django.urls import path
from . import views

app_name='exploration'

urlpatterns = [
    path('',views.dashboard_view,name='dashboard')
]
