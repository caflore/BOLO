from django.contrib import admin

from bolo_flyers.models import BoloCategory, BoloStatus, Bolo, BoloImage, BoloSubscriber

admin.site.register(BoloCategory)
admin.site.register(BoloStatus)
admin.site.register(Bolo)
admin.site.register(BoloImage)
admin.site.register(BoloSubscriber)
