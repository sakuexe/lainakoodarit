# Generated by Django 4.1.7 on 2023-04-15 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0006_alter_event_last_update_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='release_date',
            new_name='date_added',
        ),
        migrations.AlterField(
            model_name='event',
            name='last_update',
            field=models.CharField(default='2023/04/15 09:25:14', editable=False, max_length=30),
        ),
    ]