# Generated by Django 3.1.3 on 2021-05-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_auto_20210514_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='NSE',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='about',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='director',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='parentOrg',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='usstocks',
            name='marketCap',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]