# Generated by Django 4.1.7 on 2023-03-14 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleryUser', '0003_about_username'),
        ('galleryApp', '0005_gallery_gallery_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='galleryUser.about'),
        ),
    ]
