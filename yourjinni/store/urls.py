from django.contrib import admin
from django.urls import path
from store import views
# from store.views.product_details import ProductDetail

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('home/', views.home,name='home'),
    path('account/', views.account,name='account'),
    path('bamboo-craft/', views.bamboo_craft,name='bamboo-craft'),
    path('blank/', views.blank,name='blank'),
    path('block-printed-bag/', views.block_printed_bag,name='block-printed-bag'),
    path('blog/', views.blog,name='blog'),
    path('blog-detail/', views.blog_detail,name='blog-detail'),
    path('cart/', views.cart,name='cart'),
    path('checkout/', views.checkout,name='checkout'),
    path('compare/', views.compare,name='compare'),
    path('contact/', views.contact,name='contact'),
    path('forgot-password/', views.forgot_password,name='forgot-password'),
    path('forum/', views.forum,name='forum'),
    path('forum-detail/', views.forum_detail,name='forum-detail'),
    path('jute-crafts/', views.jute_crafts,name='jute-crafts'),
    path('my-account/', views.my_account,name='my-account'),
    path('my-account-order/', views.my_account_order,name='my-account-order'),
    path('policy/', views.policy,name='policy'),
    path('product-detail/', views.product_detail,name='product-detail'),
    path('stone-carving/', views.stone_carving,name='stone-carving'),
    path('terracotta/', views.terracotta,name='terracotta'),
    path('wishlist/', views.wishlist,name='wishlist'),
    path('wooden-craft/', views.wooden_craft,name='wooden-craft'),
    path('zari-zardozi/', views.zari_zardozi,name='zari-zardozi'),
]