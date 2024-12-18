from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model representing user details, including profession,
    experience, and avatar. 
    Automatically creates a profile when a new user is registered.
    """
    INTERIOR_DESIGNER = 'Interior Designer'
    ARCHITECT = "Architect"
    GRAPHIC_DESIGNER = 'Graphic Designer'
    PAINTER = "Painter"

    PROFESSIN_CHOICES = [
        (INTERIOR_DESIGNER, 'Interior Designer'),
        (ARCHITECT, "Architect"),
        (GRAPHIC_DESIGNER, 'Graphic Designer'),
        (PAINTER, "Painter"),
    ]
    DEFAULT_PROFESSION = "Arcitect"

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    full_name = models.CharField(max_length=100, blank=True)
    about = models.TextField(blank=True)
    profession = models.CharField(
        max_length=50,
        choices=PROFESSIN_CHOICES,
        blank=False,
        default=DEFAULT_PROFESSION
    )
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)
    website = models.URLField(max_length=200, blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(
        upload_to='images/', default='../avatar_jyhi5q'
    )
    avatar_alt_text = models.CharField(
        max_length=150,
        blank=True,
        default="Users's profile picture"
        )

    class Meta:
        ordering = ['-created_at']

    def ___str__(self):
        return f"{self.owner}"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
