# Generated by Django 3.0.2 on 2020-08-10 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure', '0017_auto_20200505_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='audio',
            field=models.FileField(upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='level',
            name='video',
            field=models.FileField(upload_to='video'),
        ),
    ]