# Generated by Django 3.2.5 on 2021-07-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_bag_clothing_fashion_household_interior_kid_men_shoe_sports_women'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='bag'),
        ),
        migrations.AddField(
            model_name='clothing',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='clothing'),
        ),
        migrations.AddField(
            model_name='electronics',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='electronics'),
        ),
        migrations.AddField(
            model_name='fashion',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='fashion'),
        ),
        migrations.AddField(
            model_name='household',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='household'),
        ),
        migrations.AddField(
            model_name='interior',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='interior'),
        ),
        migrations.AddField(
            model_name='kid',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='kid'),
        ),
        migrations.AddField(
            model_name='men',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='men'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='shoe'),
        ),
        migrations.AddField(
            model_name='sports',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='sports'),
        ),
        migrations.AddField(
            model_name='women',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='women'),
        ),
        migrations.AlterField(
            model_name='men',
            name='category',
            field=models.CharField(choices=[('shirt', 'shirt'), ('t-shirt', 't-shirt'), ('bottom-wear', 'bottom-wear')], default='shirt', max_length=50),
        ),
        migrations.AlterField(
            model_name='sports',
            name='category',
            field=models.CharField(choices=[('upper', 'upper'), ('bottom-wear', 'bottom-wear')], default='upper', max_length=50),
        ),
        migrations.AlterField(
            model_name='women',
            name='category',
            field=models.CharField(choices=[('top', 'top'), ('shirt', 'shirt'), ('t-shirt', 't-shirt'), ('bottom-wear', 'bottom-wear')], default='top', max_length=50),
        ),
    ]