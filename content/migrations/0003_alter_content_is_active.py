# Generated by Django 4.1.1 on 2022-10-03 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_content_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
