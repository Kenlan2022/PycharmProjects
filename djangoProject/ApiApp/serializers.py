from rest_framework import serializers
from ApiApp.models import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #fields = ('id', 'name', 'price')
        model = Product
        fields = '__all__' #簡化寫法 所有欄位都要