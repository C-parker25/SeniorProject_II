from django.contrib import admin
from .models import Donation, Subscription, VolunteerInterest

# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','amount','timestamp')

class GeneralAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','timestamp')


admin.site.register(Donation, DonationAdmin)
admin.site.register(Subscription, GeneralAdmin)
admin.site.register(VolunteerInterest, GeneralAdmin)
