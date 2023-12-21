from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import viewsets, generics
from rest_framework.generics import ListAPIView
from rest_framework import filters
from .models import User, CodeGenerate, RegularUser, Branch
from .seralizers import UserSerializer, CodeGenerateSeralizers, RegularUserSeralizers, BranchSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('is_admin', 'user_id')


class CodeGenerateViewSet(viewsets.ModelViewSet):
    queryset = CodeGenerate.objects.all()
    serializer_class = CodeGenerateSeralizers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('code', 'user__user_id')


class RegularUserViewSet(viewsets.ModelViewSet):
    queryset = RegularUser.objects.all()
    serializer_class = RegularUserSeralizers
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('user__user_id', )


class BranchListAPIView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer