from django.contrib import admin

from .models import *


class AccountInline(admin.TabularInline):
    model = Account
    extra = 0
    filter_horizontal = ['groups']


class TermInline(admin.TabularInline):
    model = Term
    extra = 0
    filter_horizontal = ['groups']


class EventAdmin(admin.ModelAdmin):
    inlines = [AccountInline, TermInline]


class TermMatchInline(admin.TabularInline):
    model = TermMatch
    extra = 0


class TweetAdmin(admin.ModelAdmin):
    inlines = [TermMatchInline]

admin.site.register(Event, EventAdmin)
admin.site.register(AccountGroup)
admin.site.register(TermGroup)
admin.site.register(Tweet, TweetAdmin)
