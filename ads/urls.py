from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^ad/(?P<ad_id>[A-Za-z0-9]+)/$', views.ad_detail, name='ad_detail'),
    path('user_form/', views.user_form, name='user_form'),
    path('thanks/', views.thanks, name='thanks'),
    path('send_mail/', views.send_email, name='send_mail'),
    path('send_email/', views.email_form, name='send_email'),
    path('email_sent/', views.email_sent, name='email_sent'),
    path('', views.ad_list, name='ad_list'),  # 広告リストページの追加
]