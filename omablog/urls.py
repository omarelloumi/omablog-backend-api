from django.urls import path
from . import views

urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('show_blogs/',views.show_blogs, name='show_blogs'),
    path('update_blog/<int:pk>', views.update_blog, name='update_blog'),
    path('delete_blog/<int:pk>', views.delete_blog, name='delete_blog')

]