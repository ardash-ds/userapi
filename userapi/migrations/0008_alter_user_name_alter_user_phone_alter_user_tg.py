# Generated by Django 4.1.2 on 2022-11-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0007_alter_user_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='user',
            name='tg',
            field=models.CharField(max_length=64),
        ),
    ]
