# Generated by Django 5.0.4 on 2024-05-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='Image', upload_to='store/static/images/'),
        ),
    ]