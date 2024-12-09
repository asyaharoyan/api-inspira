# Generated by Django 4.2 on 2024-12-05 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='style',
            field=models.CharField(choices=[('modern', 'Modern'), ('classic', 'Classic'), ('minimalist', 'Minimalist'), ('industrial', 'Industrial'), ('contemporary', 'Contemporary'), ('art_deco', 'Art Deco'), ('mid_century_modern', 'Mid-Century Modern'), ('scandinavian', 'Scandinavian'), ('bohemian', 'Bohemian'), ('farmhouse', 'Farmhouse'), ('eclectic', 'Eclectic'), ('shabby_chic', 'Shabby Chic'), ('coastal', 'Coastal'), ('traditional', 'Traditional'), ('asian_zen', 'Asian Zen'), ('rustic', 'Rustic'), ('gothic', 'Gothic'), ('futuristic', 'Futuristic'), ('neo_classical', 'Neo-Classical'), ('abstract', 'Abstract'), ('figurative', 'Figurative'), ('still_life', 'Still Life'), ('impressionism', 'Impressionism'), ('realism', 'Realism'), ('expressionism', 'Expressionism'), ('surrealism', 'Surrealism'), ('pop_art', 'Pop Art'), ('naive_art', 'Naive Art'), ('cubism', 'Cubism')], max_length=20),
        ),
    ]