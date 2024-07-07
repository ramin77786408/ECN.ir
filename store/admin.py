from django.contrib import admin

from . import models


class GroupInline(admin.TabularInline):
    model = models.Group
    fields = ['sex', 'type1','type2']
    extra = 1

class ColorInline(admin.TabularInline):
    model = models.Color
    fields = ['color']
    extra = 3

class StyleInline(admin.TabularInline):
    model = models.Style
    fields = ['style']
    extra = 5

class DescriptionInline(admin.TabularInline):
    model = models.Description
    fields = ['description1', 'description2']
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','image', 'remained_quantity')
    inlines = [GroupInline, ColorInline, StyleInline, DescriptionInline]


# @admin.register(models.Group)
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('sex', 'type1','type2')

# @admin.register(models.Color)
# class ColorAdmin(admin.ModelAdmin):
#     list_display = ('color',)