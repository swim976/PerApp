from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class LogsMemoir(models.Model):
    name = models.CharField(verbose_name='人名', max_length=128)
    content = RichTextField(verbose_name='自传')
    content2 = RichTextUploadingField(verbose_name='自传带图')

    class Meta:
        verbose_name_plural = '自传管理'
        verbose_name = '自传信息'

    def __str__(self):
        return self.name

    #   缩短显示长度
    def 自传(self):
        if len(str(self.content)) > 15:
            return '内容太长，编辑查看：{} ...'.format(str(self.content)[0:15])
        else:
            return self.content
    自传.allow_tags = True

    def 自传带图(self):
        if len(str(self.content2)) > 15:
            return f'内容太长， 编辑查看：{str(self.content2)[0:15]} ...'
        else:
            return self.content2
    自传带图.allow_tags = True
