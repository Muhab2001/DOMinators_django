from django.contrib import admin
from .models import Activity, Registration

admin.site.register(
    [
        Activity,
        Registration,
    ]
)
