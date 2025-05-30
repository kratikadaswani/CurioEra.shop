# Generated by Django 5.2 on 2025-05-24 04:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_rename_prod_name_users_product_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users_product',
            name='user_id',
        ),
        migrations.AddField(
            model_name='users_product',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='users_product',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users_product',
            name='brand_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='users_product',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='users_product',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='users_product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='users_product',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
