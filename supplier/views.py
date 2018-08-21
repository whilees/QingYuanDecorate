from django.shortcuts import render
from rest_framework import viewsets
from supplier.serializers import *
from controller.models import *
from rest_framework.permissions import IsAuthenticated
from supplier.permissions import *


# Create your views here.


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class MaterialTypeViewSet(viewsets.ModelViewSet):
    queryset = MaterialType.objects.all()
    serializer_class = MaterialTypeSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAuthenticated, SupplierAccessPermission,)

    """
    获得和工长对应区域的仓库
    """
    def get_corresponding_area(self):
        user = self.request.user
        supplier = Supplier.objects.get(user__id=user.id)
        area = Area.objects.get(supplier__id=supplier.id)
        return area

    def get_corresponding_storage(self, area):
        try:
            storage = Storage.objects.get(area_id=area.id)
        except LookupError:
            print("there is not storage in %s" % area.name)
        if storage:
            pass
        else:
            try:
                parent_area = Area.objects.get(id=area.pid)
            except LookupError:
                print("there is not father in %s" % area.name)
            if parent_area:
                self.get_corresponding_storage(parent_area)
            else:
                return False
        return storage

    def get_storage(self):
        area = self.get_corresponding_area()
        storage = self.get_corresponding_storage(area)
        return storage

    def get_client(self):
        user = self.request.user
        supplier = Supplier.objects.get(user__id=user.id)
        organization = Organization.objects.get(supplier__id=supplier.id)
        client = Client.objects.get(organization__id=organization.id)
        return client

    def get_queryset(self):
        storage = self.get_storage()
        client = self.get_client()
        materials = Material.objects.filter(storage__id=storage.id, client__id=client.id)
        kwargs = self.request.query_params.dict()
        if kwargs:
            materials = materials.filter(**kwargs)
        return materials


class ItemTypeViewSet(viewsets.ModelViewSet):
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    """
    工长显示只和自身甲方相关联的项目
    """

    def get_queryset(self):
        supplier = Supplier.objects.get(user__id=self.request.user.id)
        client = Client.objects.get(supplier__id=supplier.id)
        items = Item.objects.filter(client__id=client.id)
        kwargs = self.request.query_params.dict()
        if kwargs:
            items = items.filter(**kwargs)
        return items


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        supplier = Supplier.objects.get(user__id=self.request.user.id)
        orders = Order.objects.filter(supplier__id=supplier.id)
        return orders


class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        print(self.request.data)
        if self.request.data:
            print(self.request.data)
            return Project.objects.get(id=self.request.data['id'])
        else:
            return Project.objects.all()


class ProjectDetailViewSet(viewsets.ModelViewSet):
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer


class ProjectFineViewSet(viewsets.ModelViewSet):
    queryset = ProjectFine.objects.all()
    serializer_class = ProjectFineSerializer
