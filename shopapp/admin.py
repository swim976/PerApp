from django.contrib import admin
from .models import ShopInfo
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


admin.site.register(ShopInfo, ShopInfoAdmin)
