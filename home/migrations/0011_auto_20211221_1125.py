# Generated by Django 2.2.10 on 2021-12-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20211221_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='desc',
            field=models.TextField(max_length=500),
        ),
        migrations.DeleteModel(
            name='Marks_Of_User',
        ),
    ]
