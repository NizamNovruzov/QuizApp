# Generated by Django 2.2.10 on 2021-12-20 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20210629_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]