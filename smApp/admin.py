from django.contrib import admin
from .models import schoolInfo


# Register your models here.
@admin.register(schoolInfo)
class schoolInfoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "schoolName",
        "schoolAddress",
        "schoolEstablished",
        "schoolEstablisher",
    ]
