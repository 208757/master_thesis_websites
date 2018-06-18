from django.conf.urls import url
from .views import LogPageView, MainPageView, end_session

urlpatterns = [
    url(r'^$', LogPageView.as_view(), name='index'),
    url(r'^web/mainpage/*$', MainPageView.as_view(), name='mainpage'),
    url(r'^web/logout/*$', end_session, name='logout'),
]
