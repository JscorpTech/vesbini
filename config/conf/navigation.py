from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Users"),
                "icon": "group",
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
            {
                "title": _("Group"),
                "icon": "group",
                "link": reverse_lazy("admin:auth_group_changelist"),
            },
        ],
    },
    {
        "title": _("Dashboard"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Maxsulot"),
                "icon": "add_shopping_cart",
                "link": reverse_lazy("admin:api_productmodel_changelist"),
            },
            {
                "title": _("Karegoriya"),
                "icon": "category",
                "link": reverse_lazy("admin:api_categorymodel_changelist"),
            },
            {
                "title": _("Teglar"),
                "icon": "numbers",
                "link": reverse_lazy("admin:api_tagmodel_changelist"),
            },
            {
                "title": _("Rang"),
                "icon": "format_color_fill",
                "link": reverse_lazy("admin:api_colormodel_changelist"),
            },
            {
                "title": _("O'lcham"),
                "icon": "eraser_size_1",
                "link": reverse_lazy("admin:api_sizemodel_changelist"),
            },
            {
                "title": _("Buyurtmalar"),
                "icon": "order_approve",
                "link": reverse_lazy("admin:api_ordermodel_changelist"),
            },
        ],
    },
    {
        "title": _("Address"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Davlat"),
                "icon": "explore_nearby",
                "link": reverse_lazy("admin:accounts_countrymodel_changelist"),
            },
            {
                "title": _("Shaxar/Tuman"),
                "icon": "globe_uk",
                "link": reverse_lazy("admin:accounts_regionmodel_changelist"),
            },
        ],
    },
    {
        "title": _("Moysklad"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("sklad"),
                "icon": "store",
                "link": reverse_lazy("admin:api_storemodel_changelist"),
            },
        ],
    },
    {
        "title": _("Boshqa"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("settings"),
                "icon": "settings",
                "link": reverse_lazy("admin:shared_settingsmodel_changelist"),
            },
            {
                "title": _("delivery-methods"),
                "icon": "delivery_truck_bolt",
                "link": reverse_lazy("admin:api_deliverymethodmodel_changelist"),
            },
            {
                "title": _("Feedback"),
                "icon": "feedback",
                "link": reverse_lazy("admin:api_feedbackmodel_changelist"),
            },
        ],
    },
]
