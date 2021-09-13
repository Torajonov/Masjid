from django.contrib import admin
from.models import*
# Register your models here.

admin.site.register(Namaz_time)
admin.site.register(Comment)
admin.site.register(Gallery)
admin.site.register(Audio)
admin.site.register(Contact)
@admin.register(Blog)
class BlogAddmin(admin.ModelAdmin):
	list_display = ['title','date']
	list_display_links = ['title']
	prepopulated_fields = {'slug':('title',)}
	
@admin.register(Sheikhs)
class ShekAddmin(admin.ModelAdmin):
	list_display = ['name','direction']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}