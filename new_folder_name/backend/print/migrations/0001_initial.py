# Generated by Django 5.1.2 on 2024-12-01 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='print_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='print_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(blank=True, max_length=125, null=True)),
                ('status', models.CharField(choices=[('success', 'success'), ('failed', 'failed'), ('pending', 'pending')], default='pending', max_length=7)),
                ('orientation', models.CharField(choices=[('portrait', 'portrait'), ('landscape', 'landscape')], default='portrait', max_length=10)),
                ('sided', models.CharField(choices=[('single', 'single'), ('double', 'double')], default='single', max_length=6)),
                ('page_side', models.CharField(choices=[('A3', 'A3'), ('A4', 'A4')], default='A4', max_length=2)),
                ('copies', models.IntegerField(default=1)),
                ('timer_start', models.DateTimeField(auto_now_add=True)),
                ('timer_end', models.DateTimeField(blank=True, null=True)),
                ('page_cost', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
