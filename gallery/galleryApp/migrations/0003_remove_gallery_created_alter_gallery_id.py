# Generated by Django 4.1.7 on 2023-03-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryApp', '0002_gallery_created_alter_gallery_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='created',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]