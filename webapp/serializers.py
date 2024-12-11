from rest_framework import serializers
from webapp.models import Product

class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id',
                  'product_name',
                  'product_price',
                  'product_description',
                  'product_vendor')
