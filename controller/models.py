from django.db import models
from django.conf import settings

# Create your models here.


class Area(models.Model):
    """
    区域表
    """
    name = models.CharField(max_length=20)
    pid = models.ForeignKey('self', null=True, on_delete=models.CASCADE)


class Organization(models.Model):
    """
    公司组织架构表
    """
    name = models.CharField(max_length=20)
    pid = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Client(models.Model):
    """
    客户表
    从公司层面讲，这里应该是客户属于哪个组。多对一。
    """
    name = models.CharField(max_length=40)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Controller(models.Model):
    """系统管理员表"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Manager(models.Model):
    """公司管理员表"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Storage(models.Model):
    """仓库表"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


class Supervisor(models.Model):
    """监理表"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    supplier = models.ManyToManyField('Supplier', null=True)


class Supplier(models.Model):
    """供应商表"""
    is_default = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

