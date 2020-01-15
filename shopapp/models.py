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
