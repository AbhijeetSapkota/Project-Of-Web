from django.urls import path
from mainapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/', views.post_detail, name='post_detail'),
    path('my-posts/', views.my_posts, name='my_posts'),
]
