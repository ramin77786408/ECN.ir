# Generated by Django 5.0.4 on 2024-07-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='Image', upload_to='static/images/store/'),
        ),
    ]