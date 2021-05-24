from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from .models import Product
from rest_framework.response import Response

from django.contrib.auth.hashers import make_password
# from .serializers import ProductSerializers, UserSerializerWithToken, UserSerializers


# write you views's code here...
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
