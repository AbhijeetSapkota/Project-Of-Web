from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_feed, name='category_feed'),
    path('my-posts/', views.my_posts, name='my_posts'),
]
