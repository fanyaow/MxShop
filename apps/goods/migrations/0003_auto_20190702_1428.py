# Generated by Django 2.0.2 on 2019-07-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180409_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='is_hot',
            field=models.BooleanField(default=False, help_text='是否热销', verbose_name='是否热销'),
        ),
    ]
