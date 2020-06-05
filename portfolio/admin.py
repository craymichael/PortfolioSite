# ======================================================================================================================
# Portfolio Website
# Copyright (C) 2016  Zachariah Carmichael
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
# ======================================================================================================================
#from django.contrib import admin


# class SectionItemInline(admin.StackedInline):
#     model = SectionItem
#     extra = 3
#
#
# class SectionInline(admin.StackedInline):
#     model = Section
#     extra = 3
#     fieldsets = [
#         (None, {'fields': ['section_title', 'order']})
#     ]
#
#
# class SectionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['section_title', 'order', 'page']})
#     ]
#     inlines = [SectionInline, SectionItemInline]
#
#
# class PageAdmin(admin.ModelAdmin):
#     inlines = [SectionInline]
#
#
# admin.site.register(Page, PageAdmin)
# admin.site.register(Section, SectionAdmin)
