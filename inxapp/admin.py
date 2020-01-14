from django.contrib import admin

from inxapp.models import UserInfo
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


# class ProxyUserInfo(resources.ModelResource):
#     class Meta:
#         model = UserInfo
#
# # Register your models here.
#
#
# @admin.register(UserInfo)
# class UserInfoAdmin(ImportExportActionModelAdmin):
#     resource_class = ProxyUserInfo
#
#     list_display = ('id', 'name', 'age', 'sex', 'tel', 'detail', 'create_time')
#     list_per_page = 15

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex', 'tel', 'detail', 'create_date']  # 显示表列
    search_fields = ['name', 'create_date']
    list_editable = ['sex', 'tel', 'detail']
    list_display_links = ['name', ]
    list_filter = []
    list_per_page = 15


admin.site.register(UserInfo, UserInfoAdmin)
