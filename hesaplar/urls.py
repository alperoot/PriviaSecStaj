from django.urls import path

from .views import SignUpView


urlpatterns = [
    path('kayit/', SignUpView.as_view(), name='kayit'),
]