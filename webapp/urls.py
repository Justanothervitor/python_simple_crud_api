from django.urls import path
from webapp import views

urlpatterns =[
    path('products',views.get_products_list, name="getProducts"),
    path('products/create',views.post_product,name="createProducts"),
    path('products/<pk>',views.get_single_product,name="getSingleProduct"),
    path('products/update/<pk>',views.get_and_update_product,name="getAndUpdate"),
    path('products/delete/<pk>',views.delete_a_product,name="deleteAProduct")
]