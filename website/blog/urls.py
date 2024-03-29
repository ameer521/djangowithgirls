from django.urls import path
from blog import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/<int:pk>/',views.post_details,name="post_detail"),
    path('contents/',views.contents,name="contents"),
    path('post/new/',views.post_new,name='post_new'),
]