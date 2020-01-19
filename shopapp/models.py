from django.db import models


# Create your models here.


class ShopInfo(models.Model):
    title = models.CharField(verbose_name='商品名称', max_length=128)
    img = models.ImageField(upload_to='shopinfo/')
    price = models.DecimalField(verbose_name='商品最低价 ', max_digits=9, decimal_places=2)
    desc = models.CharField(verbose_name='商品描述', max_length=128)
    status_choices = (
        (0, '已删除'),
        (1, '下架'),
        (2, '上架')
    )
    status = models.IntegerField(verbose_name='产品状态', choices=status_choices)
    add_time = models.DateField(verbose_name='发布时间', auto_now=True)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品管理'

    def __str__(self):
        return self.title


class AddressInfo(models.Model):
    """
    地址管理
    """
    name = models.CharField(verbose_name='收货人', max_length=128)
    phone = models.CharField(verbose_name='收货人电话', max_length=128)
    receiving_choices = (
        (0, '收货时间不限'),
        (1, '周六日/节假日收货'),
        (2, '周一到周五收货')
    )
    receiving = models.IntegerField(choices=receiving_choices, verbose_name='收货时间')
    address = models.CharField(verbose_name='收货详细地址', max_length=255)

    class Meta:
        verbose_name = '地址信息'
        verbose_name_plural = '地址管理'

    def __str__(self):
        return self.name



