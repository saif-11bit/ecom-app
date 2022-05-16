from product.models import (
    Announcement,
    Banner,
    Coupon,
    Category,
    EcomPlatform,
    EcomProduct,
    ProductAttr,
    ProductAttrValue,
    ProductType,
    Product,
    ProdMedia,
    Wishlist,
    OrderItem,
    Order,
    ProdReview,
)
from rest_framework.serializers import ModelSerializer


class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EcomPlatformSerializer(ModelSerializer):
    class Meta:
        model = EcomPlatform
        fields = '__all__'


class EcomProductSerializer(ModelSerializer):
    class Meta:
        model = EcomProduct
        fields = '__all__'


class ProductAttrSerializer(ModelSerializer):
    class Meta:
        model = ProductAttr
        fields = '__all__'


class ProductAttrValueSerializer(ModelSerializer):
    class Meta:
        model = ProductAttrValue
        fields = '__all__'


class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProdMediaSerializer(ModelSerializer):
    class Meta:
        model = ProdMedia
        fields = '__all__'


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProdReviewSerializer(ModelSerializer):
    class Meta:
        model = ProdReview
        fields = '__all__'
