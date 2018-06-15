from django.contrib import admin
from .models import User, Item, Result


class ItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'name', 'link', 'details', 'add_time', 'update_time')


admin.site.register(User)
admin.site.register(Item, ItemAdmin)
admin.site.register(Result)
