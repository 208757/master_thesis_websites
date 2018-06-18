from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/$', views.LoginView.as_view()),
    url(r'notify/$', views.NotifierView.as_view()),
    url(r'check/$', views.CheckerView.as_view())
]
