# Generated by Django 4.0.4 on 2022-06-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sub_titulo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
