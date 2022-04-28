from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from api.views import check,products_detail, products,shop_list, prod_by_category, prod_by_shop, cities, shop_by_city, create_order, order_list
urlpatterns=[
    path('login/', obtain_jwt_token),
    path('shops/', shop_list), # Список всех магазинов, внезависимости от города
    path('shops/<int:shop_id>/categories/', prod_by_category), # Все категории определенного магазина
    path('shops/<int:shop_id>/categories/<int:categ_id>/products/', products.as_view()), # Все продукты определенного магазина и категории
    path('shops/<int:shop_id>/products/', prod_by_shop), # Все продукты магазина, внезависимости от категории
    path('shops/<int:shop_id>/products/<int:prod_id>/', products_detail.as_view()), # Детали продукта, определенного магазина
    path('cities/', cities), # Абсолютно все города
    path('cities/<int:city_id>/',shop_by_city), # Магазины по городу
    path('order/',create_order),
    path('order_c/', order_list),
]