from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.homepage, name='homepage'),
    path('view_polls/', views.view_polls, name='view_polls'),
    path('create-poll/', views.create_poll, name='create_poll'),
    path('<int:poll_id>/', views.vote, name='vote'),
    path('poll/<int:poll_id>/', views.view_poll, name='view_poll'),
    
]



