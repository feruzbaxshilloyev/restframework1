from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


def home(request):
    return render(request, 'home.html')


class CreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdateDestroyView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
