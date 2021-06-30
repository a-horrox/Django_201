from django.urls import path

from . import views

app_name = 'feed'

urlpatterns = {
    path("", views.HomeView.as_view(), name='index')
}
