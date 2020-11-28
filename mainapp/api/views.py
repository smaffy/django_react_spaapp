# from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from .serializers import (
    BlogCategorySerializer,
    BlogPostSerializer,
    BlogPostRetrieveSerializer,
    BlogCategoryDetailSerializer,
)
from ..models import BlogCategory, BlogPost


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

    action_to_serializer = {
        "retrieve": BlogCategoryDetailSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class,
        )


class BlogPostViewSet(viewsets.ModelViewSet):
    # queryset = BlogPost._base_manager.all()
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    action_to_serializer = {
        "list": BlogPostRetrieveSerializer,
        "retrieve": BlogPostRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class,
        )



# class TestAPIView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         data = [{"id": 1, "name": "Jeremy"}, {"id": 2, "name": "Valery"}]
#         return Response(data)
#
#



