from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from api_inspira.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    PostList view for listing posts or creating a post
    if the user is logged in. 
    The perform_create method ensures the post is associated
    with the logged-in user.
    Filters and search options are available for narrowing
    down the posts by various criteria.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
        ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'style',
        'location',
        'area_type',
    ]
    search_fields = [
        'owner__username',
        'title',
        'style',
        'area_type',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at'
        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    PostDetail view for retrieving, updating, or deleting a post.
    Only the owner can edit or delete the post.
    The view also includes the total number of likes
    and comments associated with the post.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')


class PostStyleChoice(generics.GenericAPIView):
    """
    PostStyleChoice view for retrieving the available
    post style choices in a read-only format.
    """
    def get(self, request, *args, **kwargs):
        style_choices = [choice[0] for choice in Post.STYLE_CHOICES]
        return Response(style_choices)


class PostAreaChoice(generics.GenericAPIView):
    """
    PostAreaChoice view for retrieving the available
    post area type choices in a read-only format.
    """
    def get(self, request, *args, **kwargs):
        area_type_choices = [choice[0] for choice in Post.AREA_TYPE_CHOICES]
        return Response(area_type_choices)
