from django.shortcuts import render

from rest_framework import viewsets
from .models import Link
from .serializers import LinkSerializer
from django.views.generic.edit import CreateAPIView
from django.views.generic.detail import RetrieveAPIView
from django.views.generic.edit import UpdateAPIView
from django.views.generic.edit import DestroyAPIView
from django.views.generic.list import ListAPIView
# Create your views here.
class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer