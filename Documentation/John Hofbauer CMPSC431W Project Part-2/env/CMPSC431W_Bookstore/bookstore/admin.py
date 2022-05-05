from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Comments)
admin.site.register(Usefulness)
admin.site.register(Order)
admin.site.register(TrustFactor)
