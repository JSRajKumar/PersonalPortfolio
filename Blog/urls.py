from django.urls import path
from . import views

app_name = 'Blog'
urlpatterns = [
path('', views.all_Blog, name='all_Blog'),
path('<int:Blog_id>/', views.Detail, name='Detail'),
]