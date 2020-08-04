from django.urls import path

from . import views

urlpatterns = [
    # ex: /IEMW/
    path('', views.index, name='index'),
    # ex: /IEMW/target/5
    #path('target/<int:target_id>/', views.detail, name='detail'),
    # ex: /IEMW/user/4
    path('user/<int:user_id>/', views.detail, name='detail'),
]