from rest_framework.permissions import IsAuthenticated

from core.abstract.viewsets import AbstractViewSet
from core.post.models import Post
from core.post.serializers import PostSerializer


class PostViewSet(AbstractViewSet):
    http_method_names = ('post', 'get')
    permissions_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        """Devuelve todas las publicaciones"""
        return Post.objects.all()

    def get_object(self):
        """Devuelve un objeto de publicación utilizando el public_id"""
        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])  
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        """Crea una publicación"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)