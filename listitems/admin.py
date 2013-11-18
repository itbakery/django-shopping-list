from django.contrib import admin
from listitems.models import ListItem

class ListItemAdmin(admin.ModelAdmin):
    list_display = ('username', 'listitem', 'purchased')

    def username(self, obj):
        return '%s'%(obj.user.username)


admin.site.register(ListItem, ListItemAdmin)