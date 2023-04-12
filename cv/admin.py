from django.contrib import admin

from cv.models import Profiles, Projects, Location, Languages, Skills, Certificates, Education, Work, Basics

# Register your models here.
admin.site.register(Profiles)
admin.site.register(Projects)
admin.site.register(Location)
admin.site.register(Languages)
admin.site.register(Skills)
admin.site.register(Certificates)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Basics)