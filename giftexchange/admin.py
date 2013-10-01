from django.contrib import admin
from models import Participant, Exchange

class ParticipantAdmin(admin.ModelAdmin):
    pass

class ExchangeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Participant)
admin.site.register(Exchange)