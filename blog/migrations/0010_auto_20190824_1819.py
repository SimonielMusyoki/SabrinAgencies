# Generated by Django 2.2.3 on 2019-08-24 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190824_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='UnitID',
            field=models.ForeignKey(default=1, help_text='The unit this tenant occupies', on_delete=django.db.models.deletion.CASCADE, to='blog.Units'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='units',
            name='PropertyID',
            field=models.ForeignKey(help_text='The property number where this unit exists', on_delete=django.db.models.deletion.CASCADE, to='blog.Properties'),
        ),
    ]
