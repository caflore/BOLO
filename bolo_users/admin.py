from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from bolo_users.models import User, Agency, Unit, Rank, AgencySubscribing

class UserAdmin(UserAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name', 'agency', 'date_joined','last_login')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'agency')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)
admin.site.register(Rank)
admin.site.register(Agency)
admin.site.register(AgencySubscribing)
admin.site.register(Unit)
