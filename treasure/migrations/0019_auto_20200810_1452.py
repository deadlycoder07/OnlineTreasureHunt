# Generated by Django 3.0.2 on 2020-08-10 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0018_auto_20200810_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.ImageField(default='images/sr1.jpg', upload_to='images'),
        ),
    ]
