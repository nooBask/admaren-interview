# Generated by Django 4.2.1 on 2023-06-05 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_tags_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
