from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "phone",
        "telegram",
        "is_active",
        "date_joined",
        "last_login",
    )
    list_display_links = ("id", "email")
    list_editable = (
        "is_active",
        "phone",
        "telegram",
    )
    search_fields = ("email", "phone", "telegram")
    list_filter = (
        "is_active",
        "date_joined",
        "last_login",
    )
    readonly_fields = ("date_joined", "last_login")
    ordering = ("id",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "phone",
                    "telegram",
                    "first_name",
                    "last_name",
                    "is_active",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": ("is_staff", "is_superuser", "groups", "user_permissions"),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": ("last_login", "date_joined"),
            },
        ),
        # (
        #     _("Password"),
        #     {
        #         "fields": ("password",),
        #     },
        # ),
    )
