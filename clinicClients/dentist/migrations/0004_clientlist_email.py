# Generated by Django 4.1.2 on 2022-10-09 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0003_alter_clientlist_timing'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientlist',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=200),
        ),
    ]
