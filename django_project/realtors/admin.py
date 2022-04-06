from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)

# name = models.CharField(max_length=50)
#     photo = models.ImageField(upload_to='photos/%Y/%M/%d/')
#     description = models.TextField(blank=True)
#     email = models.CharField(max_length=50)
#     phone = models.CharField(max_length=20)
#     is_mvp = models.BooleanField(default=False)
#     hire_date = models.DateTimeField(default=datetime.now, blank=True)