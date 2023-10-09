from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-form', views.get_contact, name='get_contact'),
    path('thanks/', views.move_to_thanks_page, name='move_to_thanks_page'),
    path('blog-form', views.get_blog, name="get_blog"),
    path('product-form', views.get_product, name="get_product"),
    path('list-product/', views.get_list_product, name="get_list_product"),
]
