from django.urls import path

from . import views
from hesaplar.views import SignUpView
from Posts.views import publish_post, publish_comment, update_status


urlpatterns = [

    path('basliklar/', views.index, name='index'),
    # path('basliklar/<int:post_id>/', views.detail, name='post'),
    # path('basliklar/<int:comment_id>/comment/', views.comment, name='comment'),
    path('kayit/', SignUpView.as_view(), name='kayit'),
    path('gonderi/', publish_post, name='gonderi'),
    path('basliklar/<int:post_id>/', publish_comment, name='yorum'),
    path('profil/', update_status, name='profil')
]