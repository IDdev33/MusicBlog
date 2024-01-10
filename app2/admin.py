from django.contrib import admin
from .models import Subscriber
from .models import Article

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(Article)