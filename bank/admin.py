from django.contrib import admin
admin.site.site_header="Bank of GRIP Admin"

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_id', 'contact', 'balance']
    search_fields = ['username']


class DepositAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_id', 'contact', 'amount']
    search_fields = ['username']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_id', 'contact', 'amount', 'action', 'status']
    search_fields =['username']

# Register your models here.

from .models import User
admin.site.register(User, UserAdmin)

from .models import Deposit
admin.site.register(Deposit, DepositAdmin)

from .models import History
admin.site.register(History, HistoryAdmin)



