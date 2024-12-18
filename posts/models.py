from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model representing user-generated posts with fields
    for title, content, image, style, area type, location
    and completion date.
    Includes relationship to the 'owner' (User) and timestamps,
    with default ordering by creation date.
    """
    STYLE_CHOICES = [
        ('modern', 'Modern'),
        ('classic', 'Classic'),
        ('minimalist', 'Minimalist'),
        ('industrial', 'Industrial'),
        ('contemporary', 'Contemporary'),
        ('art_deco', 'Art Deco'),
        ('mid_century_modern', 'Mid-Century Modern'),
        ('scandinavian', 'Scandinavian'),
        ('bohemian', 'Bohemian'),
        ('farmhouse', 'Farmhouse'),
        ('eclectic', 'Eclectic'),
        ('shabby_chic', 'Shabby Chic'),
        ('coastal', 'Coastal'),
        ('traditional', 'Traditional'),
        ('asian_zen', 'Asian Zen'),
        ('rustic', 'Rustic'),
        ('gothic', 'Gothic'),
        ('futuristic', 'Futuristic'),
        ('neo_classical', 'Neo-Classical'),
        ('abstract', 'Abstract'),
        ('figurative', 'Figurative'),
        ('still_life', 'Still Life'),
        ('impressionism', 'Impressionism'),
        ('realism', 'Realism'),
        ('expressionism', 'Expressionism'),
        ('surrealism', 'Surrealism'),
        ('pop_art', 'Pop Art'),
        ('naive_art', 'Naive Art'),
        ('cubism', 'Cubism'),
    ]

    AREA_TYPE_CHOICES = [
        ('interior', 'Interior'),
        ('exterior', 'Exterior'),
        ('landscape', 'Landscape'),
        ('urban', 'Urban'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', blank=False
    )
    style = models.CharField(
        max_length=20,
        choices=STYLE_CHOICES,
        blank=False
        )
    area_type = models.CharField(
        max_length=50,
        choices=AREA_TYPE_CHOICES,
        blank=True
        )
    location = models.CharField(max_length=255, blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
