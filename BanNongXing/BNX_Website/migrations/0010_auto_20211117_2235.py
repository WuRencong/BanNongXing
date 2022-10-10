# Generated by Django 2.2.4 on 2021-11-17 14:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BNX_Website', '0009_auto_20211117_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soilmess',
            name='createdTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='soilseedmess',
            name='createdTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='subclassmess',
            name='createdTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
    ]