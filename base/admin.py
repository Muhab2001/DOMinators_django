from django.contrib import admin
from .models import UserProfile, Club

admin.site.register(
    [
        Club,
    ]
)


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ["user"]
