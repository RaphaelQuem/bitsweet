# Generated by Django 2.2.6 on 2019-11-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_img_url',
            field=models.CharField(max_length=300, null=True),
        ),
    ]