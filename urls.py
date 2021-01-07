"""  Define URL patterns for blog_app """
from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # New Post
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/', views.edit_post, name = 'edit_post')
]
