from django.contrib import admin
from .models import MostActiveStock
from .models import GainerStock
from. models import LoserStock

# Register your models here.
admin.site.register(MostActiveStock)
admin.site.register(GainerStock)
admin.site.register(LoserStock)

