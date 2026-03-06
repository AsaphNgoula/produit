from django.urls import path
from products.views import productCreate, products_list,modifier,table, deleteProduct


urlpatterns = [
    path('', products_list, name='products_list'),
    path('create', productCreate, name='create'),
    path('update/<int:my_id>', modifier, name='update'),
    path('table', table, name='table'),
    path('delete/<int:my_id>', deleteProduct, name='delete')

]
