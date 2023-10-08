from django.contrib import admin
from .models import (
    Category,
    Product,
    ProductAttr,
    ProductAttrValue,
    ProductType,
    ProdMedia,
    EcomPlatform,
    EcomProduct,
    Banner,
    Coupon,
    Announcement,
    Wishlist,
    OrderItem,
    Order,
    ProdReview,
)
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductAttr)
admin.site.register(ProductAttrValue)
admin.site.register(ProductType)
admin.site.register(ProdMedia)
admin.site.register(EcomPlatform)
admin.site.register(EcomProduct)
admin.site.register(Banner)
admin.site.register(Coupon)
admin.site.register(Announcement)
admin.site.register(Wishlist)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ProdReview)
