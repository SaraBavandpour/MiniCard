from django.urls import path
from . import views

urlpatterns = [
    path('snippet_create/', views.snippet_create, name='snippet_create'),
    path('receive_user_data/', views.receive_user_data, name='receive_user_data'),
    path('snippet_list/', views.snippet_list, name='snippet_list'),
]
