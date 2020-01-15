# Generated by Django 2.2 on 2020-01-15 06:16

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogsMemoir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='人名')),
                ('content', ckeditor.fields.RichTextField(verbose_name='自传')),
                ('content2', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='自传带图')),
            ],
            options={
                'verbose_name': '自传信息',
                'verbose_name_plural': '自传管理',
            },
        ),
    ]