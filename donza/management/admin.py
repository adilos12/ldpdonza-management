from django.contrib import admin

from .models import Lid, Functie, Ouder, Ploeg, PloegLid, Seizoen

admin.site.register(Lid)
admin.site.register(Functie)
admin.site.register(Ouder)
admin.site.register(Ploeg)
admin.site.register(PloegLid)
admin.site.register(Seizoen)