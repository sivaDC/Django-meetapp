from django.contrib import admin

# Register your models here.
from .models import Meetup, Location

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    list_filter = ('location',)
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Location)