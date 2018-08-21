from rest_framework import serializers
from django.contrib.auth.models import User
from controller.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        #fields = ('url', 'username', 'email', 'groups')
        fields = '__all__'