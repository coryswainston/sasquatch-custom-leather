from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^products/$', views.shop, name="shop"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^checkout/$', views.checkout, name="checkout"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^values/$', views.values, name="values"),
    url(r'^products/(?P<pk>\d+)/$', views.product_detail, name = 'product_detail'),
]
