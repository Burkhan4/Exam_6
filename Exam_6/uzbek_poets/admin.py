from django.contrib import admin
from .models import Poet

class PoetAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'death_date')
    search_fields = ('name',)
    list_filter = ('birth_date',)
    ordering = ('name',)

    def short_bio(self, obj):
        return obj.biography[:50]
    short_bio.short_description = 'Biografiya'

    def __str__(self):
        return self.name


admin.site.register(Poet, PoetAdmin)

admin.site.site_header = "Uzbek Poets Admin"
admin.site.site_title = "Shoirlar Paneli"
admin.site.index_title = "Boshqaruv paneliga xush kelibsiz"
