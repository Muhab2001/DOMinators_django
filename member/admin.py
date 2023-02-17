from django.contrib import admin
from .models import Committee, Membership

admin.site.register(
    [
        Committee,
        Membership,
    ]
)
