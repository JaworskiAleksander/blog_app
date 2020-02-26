from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    
]
