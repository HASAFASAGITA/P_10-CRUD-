# Generated by Django 4.1 on 2022-10-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0010_prodifkip'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodifkip',
            name='nama',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prodifkip',
            name='kajur',
            field=models.CharField(max_length=50),
        ),
    ]