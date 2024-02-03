from django.contrib import admin

from blocks.models import Category, Idea, List, Notes, Periodic, Summary

admin.site.register(Notes)
admin.site.register(Summary)
admin.site.register(Periodic)
admin.site.register(List)
admin.site.register(Idea)
admin.site.register(Category)