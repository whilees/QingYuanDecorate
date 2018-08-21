from rest_framework import serializers
from manager.models import *
from controller.serializers import *


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class AS(serializers.RelatedField):
    def to_representation(self, value):
        return value.pid.id


class MaterialTypeSerializer(serializers.ModelSerializer):
    #pid = AS(read_only=True)
    child = serializers.SerializerMethodField()

    class Meta:
        model = MaterialType
        fields = ('id', 'name', 'pid','child')

    def get_child(self, obj):
        return obj.id

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    unit = serializers.StringRelatedField()
    storage = serializers.StringRelatedField()

    class Meta:
        model = Material
        fields = ('number', 'name', 'type', 'brand', 'size', 'image',
                  'selling_price', 'unit', 'stock', 'storage')


class ItemTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemType
        fields = ('id', 'name')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('number', 'name', 'type', 'supplier_price', 'client')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    project_item = serializers.SerializerMethodField()
    #test = serializers.CharField()

    def get_project_item(self, obj):
        a = obj
        b = obj.supplier.organization
        return a.supplier.id

    class Meta:
        model = Project
        #fields = '__all__'
        fields = ('id', 'address', 'number', 'client', 'project_item',)


class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectDetail
        fields = '__all__'


class ProjectFineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectFine
        fields = '__all__'
