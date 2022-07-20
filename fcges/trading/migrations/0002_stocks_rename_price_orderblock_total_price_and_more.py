# Generated by Django 4.0.6 on 2022-07-19 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_id', models.IntegerField(auto_created=True)),
                ('stock_name', models.CharField(max_length=20)),
                ('stock_code', models.CharField(max_length=5)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Stocks',
                'db_table': 'stocks',
            },
        ),
        migrations.RenameField(
            model_name='orderblock',
            old_name='price',
            new_name='total_price',
        ),
        migrations.AlterField(
            model_name='orderblock',
            name='order_id',
            field=models.IntegerField(auto_created=True),
        ),
    ]