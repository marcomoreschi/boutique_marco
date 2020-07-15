# Generated by Django 3.0.8 on 2020-07-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='has_price',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
