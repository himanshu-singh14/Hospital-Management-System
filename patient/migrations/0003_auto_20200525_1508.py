# Generated by Django 2.2.2 on 2020-05-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20200525_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='case_paper',
            field=models.IntegerField(default=1, verbose_name='Case Paper'),
        ),
    ]
