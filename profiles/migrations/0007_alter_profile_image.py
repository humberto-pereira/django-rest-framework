# Generated by Django 3.2.22 on 2024-01-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://res.cloudinary.com/h-pereira/image/upload/v1/media/images/default_profile_qxupvm', upload_to='images/'),
        ),
    ]
