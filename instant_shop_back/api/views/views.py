from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from api.models import Product, Category, Shop, City,Order
from api.serializers import ProductSerializer, ShopSerializers, CitySerializers, CategorySerializer, OrderSerializers


class products(APIView):
    def get_object(self, shop_id, categ_id):
        try:
            return Product.objects.filter(category_id=categ_id).filter(shop_id=shop_id)
        except Product.DoesNotExist as e:
            raise Http404

    def get(self, request, shop_id=None, categ_id=None):
        print(Order.objects.all())
        product = self.get_object(shop_id, categ_id)
        serializer = ProductSerializer(product, many=True)
        permission_classes = (IsAuthenticated,)
        return Response(serializer.data)


class products_detail(APIView):
    def get_object(self, prod_id, shop_id):
        try:
            return Product.objects.filter(id=prod_id).filter(shop_id=shop_id)
        except Product.DoesNotExist as e:
            raise Http404

    def get(self, request, prod_id=None, shop_id=None):
        product = self.get_object(prod_id, shop_id)
        serializer = ProductSerializer(product, many=True)
        permission_classes = (IsAuthenticated,)
        return Response(serializer.data)


@api_view(['GET'])
def shop_list(request):
    if request.method == 'GET':
        shop = Shop.objects.all()
        serializer = ShopSerializers(shop, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def prod_by_category(request, shop_id):
    if request.method == 'GET':
        category = Category.objects.filter(shop_id=shop_id)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def prod_by_shop(request, shop_id):
    if request.method == 'GET':
        products = Product.objects.filter(shop_id=shop_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def cities(request):
    if request.method == 'GET':
        city = City.objects.all()
        serializer = CitySerializers(city, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def shop_by_city(request, city_id):
    if request.method == 'GET':
        shop = Shop.objects.filter(city_id=city_id)
        serializer = ShopSerializers(shop, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        permission_classes = (IsAuthenticated,)
        serializer = OrderSerializers(data=request.data)
        print(request.data['prod'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET'])
def order_list(request):
    if request.method == 'GET':
        order = Order.objects.all()

        serializer = OrderSerializers(order, many=True)
        return Response(serializer.data)



def check(request):
    print(Shop.objects.all())