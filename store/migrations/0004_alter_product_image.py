# Generated by Django 5.0.4 on 2024-07-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='Image', upload_to='./static/images/store/'),
        ),
    ]
