"""
URL configuration for eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from anasayfa.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from anasayfa.views import index, checkout_view, cart_view, shop_view, product_details_view, blog_list_view, blog_single_view, contact_us_view, account_view, wishlist_view, custom_404, login_signup_view
from django.views.defaults import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('account/', account_view, name="account"),
    path('wishlist/', wishlist_view, name='wishlist'),
    path('checkout/', checkout_view, name='checkout'),
    path('cart/', cart_view, name='cart'),
    path('login/', login_signup_view, name='login'),
    path('shop/', shop_view, name='shop'),
    path('product-details/', product_details_view, name='product-details'),
    path('blog/', blog_list_view, name='blog-list'),
    path('blog_single/', blog_single_view, name='blog-single'),
    path('404/', custom_404, name='custom_404'),
    path('contact_us/', contact_us_view, name='contact-us'),   
]

handler404 = page_not_found 

urlpatterns += staticfiles_urlpatterns()
