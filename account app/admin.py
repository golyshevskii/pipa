# импорт модуля datetime для работы с датой и временем в методе queryset
# import of the datetime module for working with date and time in the queryset method
import datetime
from django.contrib import admin
# импорт метода send_activation_notification для формирования и отправки письма активации пользователя
# import of the send_activation_notification method to generate and send a user activation letter
from .utilities import send_activation_notification
from .models import Profile


# метод для отправки писем пользователям, которые не прошли активацию
# method for sending emails to users who did not pass activation
def send_activation_notifications(modeladmin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
        modeladmin.message_user(request, 'requirement letters sent')


send_activation_notifications.short_description = 'sending activation requests'


# класс для фильтрации пользователей прошедших и не прошедших активацию
# class for filtering users who passed and did not pass activation
class NonactivatedFilter(admin.SimpleListFilter):
    title = 'Activated?'
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return ('activated', 'done'), ('threedays', '3 days'), ('week', 'week')

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)
        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=l)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)


# класс представления информации о пользователях на странице администрации
# class for presenting information about users on the administration page
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonactivatedFilter,)
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('send_messages', 'is_active', 'is_activated'),
              ('is_staff', 'is_superuser'), 'groups', 'user_permissions',
              ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications,)


admin.site.register(Profile, ProfileAdmin)
