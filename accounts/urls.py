from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', home, name="home"),
    path('login', handlelogin, name="handlelogin"),
    path('signup', handlesignup, name="handlesignup"),
    path('logout', handlelogout, name="handlelogout"),
    path('prof', prof, name="prof"),
    path('update_profile', update_profile, name="update_profile"),
    path('All_products', All_products, name="All_products" ),
    path('shop/<str:slug>/', shop, name="shop"),
    path('product', product, name="product"),
    path('contact', contact, name="contact"),
    path('checkout', checkout, name="checkout"),
    path('cart', cart, name="cart"),
    path('blogs', blogs, name="blogs"),
    path('blog', blog, name="blog"),
    path('m', m, name="m"),
    path('manageadd', manageadd, name="manageadd"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)