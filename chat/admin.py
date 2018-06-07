from django.contrib import admin
from .models import Category, Chat
# Register your models here.


class ChatAdmin(admin.ModelAdmin):
    list_display = ('category', 'question', 'answer', 'verify')
    list_filter = ['verify', 'category']


admin.site.register(Category)
admin.site.register(Chat, ChatAdmin)
