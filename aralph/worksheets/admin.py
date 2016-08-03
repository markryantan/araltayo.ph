from django.contrib import admin

from worksheets.models import Material

class MaterialAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "link", "type", "level", "subject", "thumbnail"]
    search_fields = ["title", "description", "type", "level", "subject"]

admin.site.register(Material, MaterialAdmin)
