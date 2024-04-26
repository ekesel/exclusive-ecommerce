from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    discount_percentage = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id','price','discount_percentage','discounted_price', 'image', 'name']

    def get_discount_percentage(self, instance):
        return int(((instance.price - instance.discounted_price) / instance.price) * 100)
    
    def get_image(self, instance):
        image_obj = instance.product_images.filter(display_image=True).last()
        if image_obj:
            return image_obj.image_url
        return None

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = subCategory
        fields = ['id','name','image_url']


# class AddCommentSerializer(serializers.Serializer):
#     comment = serializers.CharField()
