from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from profiles.models import Profile


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the current user, extending UserDetailsSerializer
    to include profile-related fields 
    such as profile ID, avatar URL, and profession with validation
    for profession choices.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.avatar.url')
    profession = serializers.ChoiceField(
        source='profile.profession',
        choices=Profile.PROFESSIN_CHOICES,
        required=True,
    )

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 'profession',
        )
