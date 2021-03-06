# Generated by Django 4.0.1 on 2022-01-08 02:31

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('sales_channel', models.CharField(choices=[('1', 'Online'), ('2', 'Offline')], default='1', max_length=20)),
                ('order_priority', models.CharField(choices=[('1', 'H'), ('2', 'C'), ('3', 'L'), ('4', 'M')], default='1', max_length=20)),
                ('order_date', models.DateField()),
                ('ship_date', models.DateField()),
                ('unit_sold', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('unit_cost', models.IntegerField()),
                ('itemType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.category')),
            ],
        ),
    ]
