from django.contrib import admin
from forbot.bot.models import Offer, Requirement, TemplateText, User, Vacancy


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
        "username",
    )
    search_fields = (
        "external_id",
        "username",
    )


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
    )
    search_fields = ("title",)


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
    )
    search_fields = (
        "description",
        "vacancy__title",
    )


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
    )
    search_fields = (
        "description",
        "vacancy__title",
    )


@admin.register(TemplateText)
class TemplateTextAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "text",
    )
    search_fields = (
        "name",
        "text",
    )
