# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from fias.models import (
    NormDoc,
    SocrBase,
    NDocType,
    ActStat, CenterSt, CurentSt,
    EstStat, HSTStat, IntvStat,
    OperStat, StrStat,
)


class ViewAdmin(admin.ModelAdmin):
    """
    Класс админки только для просмотра данных модели
    """
    change_form_template = 'admin/view_form.html'
    save_on_top = False
    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass


@admin.register(SocrBase)
class SocrBaseAdmin(admin.ModelAdmin):
    list_display = ['level', 'scname', 'socrname', 'item_weight']
    list_display_links = ('scname', 'socrname')
    readonly_fields = ['level', 'scname', 'socrname', 'kod_t_st']
    list_editable = ['item_weight']
    ordering = ['-item_weight', 'level']

    actions = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(NDocType)
class NDocTypeAdmin(ViewAdmin):
    list_display = ('ndtypeid', 'name')
    list_display_links = ('name',)


@admin.register(NormDoc)
class NormDocAdmin(ViewAdmin):
    list_display = ('normdocid', 'docdate', 'docnum')
    list_display_links = ('docnum',)


@admin.register(ActStat)
class ActStatAdmin(ViewAdmin):
    list_display = ('actstatid', 'name')
    list_display_links = ('name',)


@admin.register(CenterSt)
class CenterStatAdmin(ViewAdmin):
    list_display = ('centerstid', 'name')
    list_display_links = ('name',)


@admin.register(CurentSt)
class CurentStatAdmin(ViewAdmin):
    list_display = ('curentstid', 'name')
    list_display_links = ('name',)


@admin.register(EstStat)
class EstStatAdmin(ViewAdmin):
    list_display = ('eststatid', 'name', 'shortname')
    list_display_links = ('name',)


@admin.register(HSTStat)
class HSTStatAdmin(ViewAdmin):
    list_display = ('housestid', 'name')
    list_display_links = ('name',)


@admin.register(IntvStat)
class IntvStatAdmin(ViewAdmin):
    list_display = ('intvstatid', 'name')
    list_display_links = ('name',)


@admin.register(OperStat)
class OperStatAdmin(ViewAdmin):
    list_display = ('operstatid', 'name')
    list_display_links = ('name',)


@admin.register(StrStat)
class StrStatAdmin(ViewAdmin):
    list_display = ('strstatid', 'name', 'shortname')
    list_display_links = ('name',)
