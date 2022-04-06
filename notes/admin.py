from django.contrib import admin
from .models import Notes
from groups.models import NotesGroups

# Register your models here.

class NotesAdmin(admin.ModelAdmin):
  readonly_fields = ('date_create',)

class NotesGroupsAdmin(admin.ModelAdmin):
  readonly_fields = ('date_create',)

admin.site.register(Notes, NotesAdmin)
admin.site.register(NotesGroups, NotesGroupsAdmin)