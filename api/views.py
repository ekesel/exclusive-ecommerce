from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import *
from constance import config as constance_config
from api.models import Category, Product, subCategory
from .serializers import ProductSerializer, SubCategorySerializer
from django.db.models import Count

# Create your views here.

@api_view(['GET'])
@permission_classes(())
def homepageconfigs(request):
    if request.method == 'GET':
        image_banner = constance_config.IMAGE_BANNER
        flash_product_queryset = Product.objects.filter(is_active=True, flash_sale=True)
        flash_products = ProductSerializer(flash_product_queryset, many=True)
        sub_category_queryset = subCategory.objects.exclude(image_url=None, name=None)
        sub_categories = SubCategorySerializer(sub_category_queryset, many=True)
        products_with_order_count = Product.objects.annotate(order_count=Count('product_orders'))
        products_ordered_by_orders = products_with_order_count.order_by('-order_count')
        explore_products = ProductSerializer(Product.objects.all()[:10], many=True)
        best_selling_products = ProductSerializer(products_ordered_by_orders, many=True)
        new_arrivals = [constance_config.NEW_ARRIVAL_BANNER_1, constance_config.NEW_ARRIVAL_BANNER_2, 
                        constance_config.NEW_ARRIVAL_BANNER_3, constance_config.NEW_ARRIVAL_BANNER_4]
        data = {
            'categories': list(Category.objects.all().values_list('name', flat=True)),
            'image_banner': image_banner,
            'flash_products': flash_products.data,
            'sub_categories': sub_categories.data,
            'new_arrivals': new_arrivals,
            'best_selling_products': best_selling_products.data,
            'explore_products': explore_products.data
        }
        return Response(data,status=200)
    return Response({},status=200)

@api_view(['GET'])
@permission_classes(())
def login_configs(request):
    if request.method == 'GET':
        support_details = {
            'address':  constance_config.ADDRESS,
            'email': constance_config.EMAIL,
            'phone': constance_config.PHONE
        }
        social_links = {
            'linkedin': constance_config.LINKEDIN_LINK,
            'instagram': constance_config.INSTAGRAM_LINK,
            'x': constance_config.X_LINK,
            'facebook': constance_config.FACEBOOK_LINK
        }
        data = {
            'top_banner': constance_config.TOP_BANNER,
            'site_name': constance_config.SITE_TITLE,
            'support_details': support_details,
            'app_details': constance_config.APP_DETAILS,
            'social_links': social_links
        }
        return Response(data,status=200)
    return Response({},status=200)