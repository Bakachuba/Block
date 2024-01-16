from django.contrib import admin

from blocks.models import Notes, Summary, Periodic, List, Idea

admin.site.register(Notes)
admin.site.register(Summary)
admin.site.register(Periodic)
admin.site.register(List)
admin.site.register(Idea)