from django.contrib import admin
from .models import Messages,Post, Projects, Properties, Units, Tenant, Vendor, Payment, Expense,Lease

admin.site.register(Post)
admin.site.register(Messages)
admin.site.register(Projects)
admin.site.register(Properties)
admin.site.register(Units)
admin.site.register(Tenant)
admin.site.register(Vendor)
admin.site.register(Payment)
admin.site.register(Expense)
admin.site.register(Lease)




# Register your models here.
