# Generated by Django 2.0.2 on 2019-07-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180414_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(blank=True, help_text='手机号', max_length=11, null=True, verbose_name='电话'),
        ),
    ]
