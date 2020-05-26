# Generated by Django 2.2.2 on 2020-05-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='case_paper',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='is_female',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='is_male',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='is_other',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='medical_report',
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.CharField(blank=True, choices=[('Neurology', 'NEUROLOGY'), ('Cardiology', 'CARDIOLOGY'), ('Emergency', 'EMERGENCY')], max_length=20, null=True, verbose_name='Department '),
        ),
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Others', 'OTHERS')], max_length=10, null=True, verbose_name='Gender '),
        ),
        migrations.AddField(
            model_name='doctor',
            name='salary',
            field=models.IntegerField(blank=True, null=True, verbose_name='Case Paper'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'ACTIVE'), ('Inactive', 'INACTIVE')], max_length=10, null=True, verbose_name='Status '),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]