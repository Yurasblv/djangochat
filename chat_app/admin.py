from django.contrib import admin
from chat_app.models import Message


class RatingAdmin(admin.ModelAdmin):
    list_display = ['__all__']


admin.site.register(Message)
