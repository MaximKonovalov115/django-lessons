# Generated by Django 3.0.4 on 2020-04-20 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200420_1617'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказа', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус заказа', 'verbose_name_plural': 'Статусы заказов'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='productinorder',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_address',
            field=models.CharField(blank=True, default=None, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='amount_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmb', models.IntegerField(default=1)),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
    ]