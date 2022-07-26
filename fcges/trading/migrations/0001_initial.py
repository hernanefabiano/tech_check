# Generated by Django 4.0.6 on 2022-07-19 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'OrderBlock',
                'db_table': 'order_block',
            },
        ),
    ]
