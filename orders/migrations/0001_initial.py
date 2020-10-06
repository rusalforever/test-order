# Generated by Django 3.1.1 on 2020-10-01 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Done', 'Done'), ('Paid', 'Paid')], default='Open', max_length=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.product')),
            ],
        ),
    ]
