from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from api_inspira.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    ProfileList view for listing all profiles with annotated counts
    for posts, followers, and following. 
    Supports filtering by relationships and ordering by
    various annotated fields.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    ProfileDetail view for retrieving or updating a specific profile. 
    Includes annotated counts for posts, followers, and following,
    with ownership-based permissions.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ProfessionChoicesList(generics.GenericAPIView):
    """
    A read-only view to list profession choices.
    """
    def get(self, request, *args, **kwargs):
        professions = [choice[0] for choice in Profile.PROFESSIN_CHOICES]
        return Response(professions)
