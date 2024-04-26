from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import *
from constance import config as constance_config
from api.models import Category, Product, subCategory, CustomerDetail
from .serializers import ProductSerializer, SubCategorySerializer
from django.db.models import Count
from rest_framework import status
from django.contrib.auth.models import User
from .utils import is_valid_email, is_valid_phone
from rest_framework.authtoken.models import Token

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

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('name')
        email_or_phone = request.data.get('email_or_phone')
        password = request.data.get('password')
        email = None
        phone = None

        if not username or not password or not email_or_phone:
            return Response({'error': 'Please provide username, email/phone and password'}, status=status.HTTP_400_BAD_REQUEST)

        is_email = is_valid_email(email_or_phone)
        is_phone = is_valid_phone(email_or_phone)

        if is_email:
            email = email_or_phone
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists, Please Login'}, status=status.HTTP_400_BAD_REQUEST)
            
        if is_phone:
            phone = email_or_phone
            if CustomerDetail.objects.filter(phone=phone).exists():
                return Response({'error': 'Phone number already exists, Please Login'}, status=status.HTTP_400_BAD_REQUEST)

        if not email and not phone:
            return Response({'error': 'Please provide valid Email or Phone'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        customer = CustomerDetail.objects.create(user=user,phone=phone)
        if user and customer:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Failed to create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email_or_phone = request.data.get('email_or_phone')
        password = request.data.get('password')
        user = None

        if not email_or_phone or not password:
            return Response({'error': 'Please provide email/phone and password'}, status=status.HTTP_400_BAD_REQUEST)

        is_email = is_valid_email(email_or_phone)
        is_phone = is_valid_phone(email_or_phone)

        if is_email:
            try:
                user = User.objects.get(email=email_or_phone)
            except User.DoesNotExist:
                return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
        elif is_phone:
            try:
                customer = CustomerDetail.objects.get(phone=email_or_phone)
                user = customer.user
            except CustomerDetail.DoesNotExist:
                return Response({'error': 'Invalid phone number or password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide valid email or phone number'}, status=status.HTTP_400_BAD_REQUEST)

        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email/phone or password'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
