from django.db import models
from helper.models import CommonBase
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel, CommonBase):
    """Category for Product: Ex: Men, Topwear, Tshirt.
    Parent denotes to self as a Category. Ex: Men > Topwear > Tshirt."""
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        if self.parent:
            return f"{self.name} -< {self.parent.name}"
        else:
            return f"{self.name}"


class ProductAttr(models.Model):
    """ProductAttr is the attribute of the product such as: Size, Color etc."""
    name = models.CharField(max_length=100)
    desc = models.TextField()
    
    def __str__(self):
        return f"{self.name}: {self.desc}"
    
    
class ProductAttrValue(models.Model):
    """ProductAttrValue consist of a attr_value with parent ProductAttr. Ex: Size-S,M,L,XL."""
    prod_attr = models.ForeignKey(ProductAttr, on_delete=models.CASCADE)
    attr_value = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.attr_value} of {self.prod_attr.name}"


class ProductType(models.Model):
    """ProductType is the collection of Attributes of a product in a place.
    Ex. Product Tshirt - Size, Color, Weight, Washable etc."""
    name = models.CharField(max_length=200)
    prod_attr = models.ManyToManyField(ProductAttr)


class Product(CommonBase):
    """Product Table with Product description, attributes and other details."""
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    cost_price = models.IntegerField()
    selling_price = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField(max_length=300)
    attr_values =  models.ManyToManyField(ProductAttrValue)
    prod_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.name}: {self.category.name}"

    
class ProdMedia(CommonBase):
    """Media files for Products"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return f'{self.product.name}'


class EcomPlatform(models.Model):
    """EcomPlatform is where business sell their product on. For ex: Amazon, Flipkart etc."""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return "{self.name}"
    

class EcomProduct(models.Model):
    """EcomProduct is the product and where else do you sell that product. 
    Ex: Blue Kurta with T-shape also available Amazon."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    platform = models.ForeignKey(EcomPlatform, on_delete=models.CASCADE)
    link = models.URLField(max_length=300)
    
    def __str__(self):
        return f"{self.platform}: {self.product}"
    
    
class Banner(CommonBase):
    """Banner/Carousel on the Website."""
    landscape_img = models.ImageField()
    seq_no = models.IntegerField()
    slug = models.SlugField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return f"{self.seq_no} - {self.category.name}"