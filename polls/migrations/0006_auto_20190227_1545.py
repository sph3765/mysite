# Generated by Django 2.1.7 on 2019-02-27 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190227_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='departmentName',
            field=models.CharField(max_length=200),
        ),
    ]
