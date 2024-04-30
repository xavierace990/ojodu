from django.contrib import admin

# Register your models here.
from .models import FeedBack
from .models import First
from .models import Teaching_sermon
admin.site.register(FeedBack)
admin.site.register(First)
admin.site.register(Teaching_sermon)

