# Generated by Django 4.2.7 on 2023-12-22 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_country_area_alter_country_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='country',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='country',
            name='inputArea',
            field=models.SlugField(),
        ),
    ]
