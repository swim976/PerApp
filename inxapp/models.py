from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=128)
    create_date = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    tel = models.CharField(verbose_name='电话', max_length=11)
    sex_choices = (
        (0, '未知'),
        (1, '男'),
        (2, '女')
    )
    detail = models.TextField(verbose_name='用户描述', null=True, blank=True, help_text='描述用户特征')
    sex = models.IntegerField(choices=sex_choices, verbose_name='性别')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户管理'

    def __str__(self):
        return self.name
