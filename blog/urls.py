from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),  
    path('post/<slug:slug>/', views.post_detail, name='post_detail'), 
    path('post/<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),  
    path('post/<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('about/', include('about.urls')),
    path("accounts/", include("allauth.urls")),
]

