from django.urls import path
from rest_framework import routers

from .views import BlogCategoryViewSet, BlogPostViewSet

router = routers.SimpleRouter()
router.register('category', BlogCategoryViewSet, basename='category')
router.register('blogpost', BlogPostViewSet, basename='blogpost')


urlpatterns = []
urlpatterns += router.urls


# from .views import TestAPIView
# path('test-api/', TestAPIView.as_view(), name='test'),
