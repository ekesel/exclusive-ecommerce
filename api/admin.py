from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(subCategory)
admin.site.register(Product)
admin.site.register(ColorVariation)
admin.site.register(SizeVariation)
admin.site.register(PincodeProductAvailability)
admin.site.register(ProductImages)
admin.site.register(Rating)
admin.site.register(CustomerDetail)
admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(GiftVoucher)
admin.site.register(BillingDetails)
admin.site.register(Lead)