import io
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Moment, Entry

class MomentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)

class EntryAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', 'moments_from_this_day')

admin.site.register(User, UserAdmin)
admin.site.register(Moment, MomentAdmin)
admin.site.register(Entry, EntryAdmin)