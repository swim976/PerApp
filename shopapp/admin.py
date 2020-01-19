from django.contrib import admin
from .models import ShopInfo, AddressInfo
# Register your models here.


class ShopInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'img', 'price', 'desc', 'status', 'add_time']
    list_display_links = []
    list_editable = []
    search_fields = []
    list_filter = []
    list_per_page = 15
    # 正序
    ordering = ['id']


class AddressInfoAdmin(admin.ModelAdmin):
    """地址管理"""
    list_display = ['id', 'name', 'phone', 'receiving', 'address']
    list_display_links = []
    list_editable = []
    search_fields = []
    list_per_page = 15


admin.site.register(AddressInfo, AddressInfoAdmin)
admin.site.register(ShopInfo, ShopInfoAdmin)
