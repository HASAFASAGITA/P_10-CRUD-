# Generated by Django 4.1 on 2022-10-11 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0012_rename_nama_prodifkip_namajurusan_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodifkip',
            old_name='tahun',
            new_name='tahunberdiri',
        ),
    ]
