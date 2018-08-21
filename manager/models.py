from django.db import models
from django.conf import settings
from controller.models import Client
from controller.models import *

# Create your models here.


class Brand(models.Model):
    """
    品牌表
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Unit(models.Model):
    """
    单位表
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class MaterialType(models.Model):
    """
    材料类别
    """
    name = models.CharField(max_length=40)
    pid = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Material(models.Model):
    """
    材料信息
    """
    number = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    type = models.ForeignKey('MaterialType', null=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    size = models.CharField(max_length=200)
    image = models.ImageField()
    opening_price = models.DecimalField(max_digits=8, decimal_places=2)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    close_time = models.DateTimeField(default=None)
    stock = models.IntegerField()
    storage = models.ForeignKey(Storage, related_name='storage', on_delete=models.CASCADE)
    storage_location = models.CharField(max_length=80)
    client = models.ManyToManyField(Client)

    def __str__(self):
        return self.name


class ItemType(models.Model):
    """
    项目类别
    """
    name = models.CharField(max_length=40)
    pid = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    项目信息
    """
    number = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    type = models.ForeignKey('ItemType', null=True, on_delete=models.CASCADE)
    client_price = models.DecimalField(max_digits=8, decimal_places=2)
    supplier_price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    close_time = models.DateTimeField(default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    corresponding_supplier = models.ForeignKey(Supplier, related_name='corresponding_supplier',
                                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    订单信息
    """
    number = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    foreman = models.ForeignKey(Supplier, related_name='oder_foreman', on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, related_name='oder_storage', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    close_time = models.DateTimeField()
    storage_receive = 'SR'
    storage_send = 'SS'
    foreman_receive = 'FR'
    storage_confirm = 'SC'
    foreman_cancel = 'FC'
    order_choices = (
        (storage_receive, 'storage received orders of foreman'),
        (storage_send, 'storage sent material to foreman'),
        (foreman_receive, 'foreman has received material'),
        (storage_confirm, 'storage confirm the order'),
        (foreman_cancel, 'oder has been cancel by foreman'),
    )
    status = models.CharField(max_length=2, choices=order_choices)
    is_close = models.BooleanField()


class OrderDetail(models.Model):
    """
    订单详细信息
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    is_received = models.BooleanField()
    received_time = models.DateTimeField()
    receive_number = models.IntegerField()


class Project(models.Model):
    """
    项目信息
    project_finish 项目已完成，监理统计实际数量
    supplier_confirm 供应商已确认实际数量
    project_close 监理确认供应商反馈数量无误，项目关闭。
    """
    number = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    default_supervisor = models.ForeignKey(Supervisor, related_name='default_supervisor',
                                           on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, related_name='supplier', on_delete=models.CASCADE)
    project_type = models.ForeignKey('ProjectType', on_delete=models.CASCADE)
    project_property = models.ForeignKey('ProjectProperty', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    expected_time = models.DateTimeField()
    finished_time = models.DateTimeField()
    supplier_confirm_time = models.DateTimeField()
    close_time = models.DateTimeField()
    project_finish = 'PF'
    supplier_confirm = 'SC'
    project_close = 'PC'
    project_choices = (
        (project_finish, 'project finished'),
        (supplier_confirm, 'supplier confirm'),
        (project_close, 'project close'),
    )
    project_status = project_choices


class ProjectDaily(models.Model):
    """
    项目日常汇报
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)


class ProjectDetail(models.Model):
    """
    项目详细清单
    expected_number 预估项目量
    actual_number 监理确认的实际数量
    supplier_number 供应商确认的实际数量
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    expected_number = models.IntegerField(null=False)
    actual_number = models.IntegerField()
    supplier_number = models.IntegerField()


class ProjectFine(models.Model):
    """
    项目的罚款
    user 罚款的对象
    money 罚款金额
    description 罚款描述
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete=models.CASCADE)
    money = models.IntegerField()
    description = models.CharField(max_length=500)


class ProjectType(models.Model):
    """
    项目的类型
    如：新收标准配置、租期配置等
    """
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)


class ProjectProperty(models.Model):
    """
    项目的属性
    如：毛坯、精装、改造等
    """
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)



