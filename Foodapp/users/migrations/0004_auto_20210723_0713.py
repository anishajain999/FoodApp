# Generated by Django 3.1.7 on 2021-07-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210722_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='profilepic.png', upload_to='profile_pictures'),
        ),
    ]