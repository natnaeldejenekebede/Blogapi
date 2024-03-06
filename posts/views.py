from rest_framework import generics, permissions 
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly 

from django.contrib.auth import get_user_model 
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser # new



from .models import Post
from .serializers import PostSerializer, UserSerializer 


class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class UserViewSet(viewsets.ModelViewSet): # new
    permission_classes = [IsAdminUser] # new

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer





class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 

    permission_classes = (permissions.IsAdminUser,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    