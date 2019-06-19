from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs_index, name='index'),
    path('blogs/<int:blog_id>/', views.blogs_detail, name='detail'),
    path('blogs/create/', views.BlogCreate.as_view(), name='blogs_create'),
    path('blogs/<int:pk>/update/', views.BlogUpdate.as_view(), name='blogs_update'),
    path('blogs/<int:pk>/delete/', views.BlogDelete.as_view(), name='blogs_delete'),
    path('blogs/<int:blog_id>/add_comment/', views.add_comment, name='add_comment'),
    path('blogs/<int:blog_id>/comments/<int:pk>/delete_comment/', views.CommentDelete.as_view(), name='delete_comment'),
]