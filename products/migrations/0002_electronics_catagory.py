# Generated by Django 3.2.5 on 2021-07-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronics',
            name='catagory',
            field=models.CharField(choices=[('mobile', 'mobile'), ('computer', 'computer'), ('tv', 'tv'), ('camera', 'camera'), ('headphones', 'headphones'), ('speakers', 'speakers')], default='mobile', max_length=50),
        ),
    ]
