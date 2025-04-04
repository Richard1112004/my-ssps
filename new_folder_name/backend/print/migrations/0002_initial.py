# Generated by Django 5.1.2 on 2024-12-01 04:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('print', '0001_initial'),
        ('printer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='print_file',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='print_order',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='print.print_file'),
        ),
        migrations.AddField(
            model_name='print_order',
            name='printer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printer.printer'),
        ),
        migrations.AddField(
            model_name='print_order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
