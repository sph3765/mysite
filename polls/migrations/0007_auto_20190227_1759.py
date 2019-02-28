# Generated by Django 2.1.7 on 2019-02-27 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20190227_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='employees',
        ),
        migrations.AddField(
            model_name='department',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Employee'),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]