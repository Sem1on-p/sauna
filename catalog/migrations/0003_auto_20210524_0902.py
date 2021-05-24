# Generated by Django 3.2 on 2021-05-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210524_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='ddqwdq', verbose_name='Описание товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/product/', verbose_name='Изображение'),
        ),
    ]