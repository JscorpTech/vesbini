from django.contrib.auth import admin
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin, StackedInline
from unfold.contrib.filters.admin import AutocompleteSelectMultipleFilter, ChoicesDropdownFilter, FieldTextFilter
from unfold.decorators import display
from unfold.forms import AdminPasswordChangeForm  # UserCreationForm,
from unfold.forms import UserChangeForm

from core.apps.accounts.models.user import Profile


class ProfileInline(StackedInline):
    model = Profile
    can_delete = False
    extra = 0
    tab = True
    verbose_name = _("Profile")
    verbose_name_plural = _("Profiles")


class CustomUserAdmin(admin.UserAdmin, ModelAdmin):
    inlines = [ProfileInline]
    change_password_form = AdminPasswordChangeForm
    list_filter_submit = True
    # add_form = UserCreationForm
    form = UserChangeForm
    list_filter = (
        ("phone", FieldTextFilter),
        ("region", AutocompleteSelectMultipleFilter),
        ("country", AutocompleteSelectMultipleFilter),
        ("role", ChoicesDropdownFilter),
    )
    search_fields = ["first_name", "phone", "last_name", "username"]
    list_display = ("first_name", "last_name", "phone", "role", "_balance")
    autocomplete_fields = ["groups", "user_permissions"]
    fieldsets = ((None, {"fields": ("phone",)}),) + (
        (None, {"fields": ("username", "password", "country", "region")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "role",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    @display(description=_("balance"), label=True)
    def _balance(self, obj):
        return "{:,.2f} so'm".format(obj.profile.balance)


class PermissionAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class GroupAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    autocomplete_fields = ("permissions",)


class SmsConfirmAdmin(ModelAdmin):
    list_display = ["phone", "code", "resend_count", "try_count"]
    search_fields = ["phone", "code"]
