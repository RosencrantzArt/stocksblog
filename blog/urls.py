from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),  
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  
]

