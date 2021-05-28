from django.urls import path

from . import views
from hesaplar.views import SignUpView
from Posts.views import publish_post, publish_comment, update_status, toggle_thread, update_post


urlpatterns = [

    path('basliklar/', views.index, name='index'),
    # path('basliklar/<int:post_id>/', views.detail, name='post'),
    # path('basliklar/<int:comment_id>/comment/', views.comment, name='comment'),
    path('kayit/', SignUpView.as_view(), name='kayit'),
    path('gonderi/', publish_post, name='gonderi'),
    path('basliklar/<int:post_id>/', publish_comment, name='yorum'),
    path('profil/', update_status, name='profil'),
    path('delete/<int:post_id>',views.delete_post,name='delete'),
    path('flushcomments/<int:post_id>', views.flush_comments, name='flush_comments'),
    path('togglethread/', toggle_thread, name='togglethread'),
    path('deletecomment/<int:comment_id>',views.delete_comment,name='delete_comment'),
    path('kullanici/<int:comment_id>',views.show_profile, name='show_profile'),
    path('updatepost/<int:post_id>', views.update_post, name='update_post'),
]