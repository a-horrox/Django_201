from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = {
    path('profile/<str:username>/', views.ProfileDetailView.as_view(), name='detail'),
    path('profile/<str:username>/follow/', views.FollowView.as_view(), name='follow'),
}




 