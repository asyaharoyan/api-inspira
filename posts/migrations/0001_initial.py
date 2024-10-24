# Generated by Django 4.2 on 2024-10-23 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('style', models.CharField(choices=[('modern', 'Modern'), ('classic', 'Classic'), ('minimalist', 'Minimalist'), ('industrial', 'Industrial'), ('contemporary', 'Contemporary'), ('art_deco', 'Art Deco'), ('mid_century_modern', 'Mid-Century Modern'), ('scandinavian', 'Scandinavian'), ('bohemian', 'Bohemian'), ('farmhouse', 'Farmhouse'), ('eclectic', 'Eclectic'), ('shabby_chic', 'Shabby Chic'), ('coastal', 'Coastal'), ('traditional', 'Traditional'), ('asian_zen', 'Asian Zen'), ('rustic', 'Rustic'), ('gothic', 'Gothic'), ('futuristic', 'Futuristic'), ('neo_classical', 'Neo-Classical'), ('abstract', 'Abstract'), ('figurative', 'Figurative'), ('still_life', 'Still Life'), ('impressionism', 'Impressionism'), ('realism', 'Realism'), ('expressionism', 'Expressionism'), ('surrealism', 'Surrealism'), ('pop_art', 'Pop Art'), ('naive_art', 'Naive Art'), ('cubism', 'Cubism')], default='Classic', max_length=20)),
                ('area_type', models.CharField(blank=True, choices=[('interior', 'Interior'), ('exterior', 'Exterior'), ('landscape', 'Landscape'), ('urban', 'Urban')], max_length=50)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
