# Generated by Django 3.2.18 on 2023-03-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customer_mst_tbl_reward_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_mst_tbl',
            name='is_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='service_mst_tbl',
            name='service_img',
            field=models.ImageField(default='noimg', upload_to='uploads/services'),
        ),
    ]
