# Generated by Django 3.1.3 on 2020-11-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0004_auto_20201119_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='email',
            field=models.EmailField(default='commuride@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
