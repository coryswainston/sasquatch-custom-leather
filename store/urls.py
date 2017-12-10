from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^shop/$', views.shop, name="shop"),
    url(r'^cart/$', views.cart, name="cart"),
    url(r'^checkout/$', views.checkout, name="checkout"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^values/$', views.values, name="values"),
]
