from django.urls import path

from . import views

urlpatterns = [

    path('basliklar/', views.index, name='index'),
    path('basliklar/<int:post_id>/', views.detail, name='post'),
    path('basliklar/<int:question_id>/comment/', views.comment, name='comment'),

]