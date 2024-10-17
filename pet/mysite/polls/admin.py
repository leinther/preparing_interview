from django.contrib import admin

from .models import Question,Choice,Persons, FileManager

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Persons)
admin.site.register(FileManager)
