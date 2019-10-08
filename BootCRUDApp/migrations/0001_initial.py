# Generated by Django 2.2.5 on 2019-10-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itm_picture', models.CharField(max_length=255)),
                ('itm_name', models.CharField(max_length=255)),
                ('itm_description', models.TextField(max_length=255)),
                ('itm_price', models.IntegerField(default=0)),
            ],
        ),
    ]