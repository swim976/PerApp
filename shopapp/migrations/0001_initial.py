# Generated by Django 2.2 on 2020-01-15 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='商品名称')),
                ('img', models.ImageField(upload_to='shopinfo/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='商品最低价 ')),
                ('desc', models.CharField(max_length=128, verbose_name='商品描述')),
                ('status', models.IntegerField(choices=[(0, '已删除'), (1, '下架'), (2, '上架')], verbose_name='产品状态')),
                ('add_time', models.DateField(auto_now=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品管理',
            },
        ),
    ]
