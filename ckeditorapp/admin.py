from django.contrib import admin
from .models import LogsMemoir
# Register your models here.


class LogsMemoirAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', '自传', '自传带图']
    list_editable = []
    search_fields = []
    list_display_links = ['id', 'name', '自传', '自传带图']
    list_per_page = 15
    # 正序
    ordering = ['id']


admin.site.register(LogsMemoir, LogsMemoirAdmin)
