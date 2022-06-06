from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^send_login_email$', views.send_login_email,
        name='send_login_email'),
    # url('^login/\u003f/token/\u003D/\w+', views.login,
    url(r'^login', views.login,
        name='login'),
    ]
