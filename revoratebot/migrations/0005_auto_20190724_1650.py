# Generated by Django 2.2.3 on 2019-07-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revoratebot', '0004_auto_20190720_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
