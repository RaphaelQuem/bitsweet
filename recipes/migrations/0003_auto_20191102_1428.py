# Generated by Django 2.2.6 on 2019-11-02 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_recipe_img_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredient',
            new_name='ingredients',
        ),
    ]