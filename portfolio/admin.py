from django.contrib import admin

from .models import Page, Section, SectionItem


class SectionItemInline(admin.StackedInline):
    model = SectionItem
    extra = 3


class SectionInline(admin.StackedInline):
    model = Section
    extra = 3
    fieldsets = [
        (None, {'fields': ['section_title', 'order']})
    ]


class SectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['section_title', 'order', 'page']})
    ]
    inlines = [SectionInline, SectionItemInline]


class PageAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


admin.site.register(Page, PageAdmin)
admin.site.register(Section, SectionAdmin)
