from django.urls import path

from . import views

app_name = 'feed'

urlpatterns = {
    path('', views.HomeView.as_view(), name='index'),
    path('my_feed/', views.HomeView.as_view(), name='my_feed'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('new/', views.CreateNewPost.as_view(), name='new_post'),
    
}
