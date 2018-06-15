from django.contrib import admin
from django.urls import path, re_path
from api.views import UserView, ItemListView, ItemView, ResultListView, ResultView
from m.views import RenderHtmlView
from dw.views import RenderDwView
from werobot.contrib.django import make_view
from mx.reply import robot


app_name = 'm'
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/user/', UserView.as_view(), name='user'),
    re_path(r'^api/item/', ItemView.as_view(), name='item'),
    re_path(r'^api/itemlist/', ItemListView.as_view(), name='itemlist'),
    re_path(r'^api/resultlist/', ResultListView.as_view(), name='resultlist'),
    re_path(r'^api/result/', ResultView.as_view(), name='result'),
    re_path(r'^$', make_view(robot), name='robot'),
    re_path(r'^m/(?P<html>.+)/', RenderHtmlView.as_view(), name='m'),
    re_path(r'^dw/(?P<random_str>.+)/', RenderDwView.as_view(), name='dw')
]
