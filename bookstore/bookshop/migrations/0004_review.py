# Generated by Django 3.0.6 on 2024-06-11 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0003_auto_20200604_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=20)),
                ('rating', models.IntegerField(default=1, max_length=5)),
                ('review_comment', models.TextField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='bookshop.Product')),
            ],
        ),
    ]
