# Generated by Django 4.1.7 on 2023-04-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0010_product_category_alter_event_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='last_update',
            field=models.CharField(default='2023/04/16 08:21:33', editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=30),
        ),
    ]