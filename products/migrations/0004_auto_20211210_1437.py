# Generated by Django 2.2.25 on 2021-12-10 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211210_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user',
            new_name='author_user',
        ),
    ]