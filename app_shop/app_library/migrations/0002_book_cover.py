# Generated by Django 4.0.1 on 2022-01-31 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover'),
        ),
    ]