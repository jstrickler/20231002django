from django.contrib import admin
# Register your models here.

# from .models import MyModel

# admin.site.register(MyModel)

from person.models import Person, City, Complaint

for model in City, Complaint:
    admin.site.register(model)

class PersonAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name', 'city__name']  #  model__field


admin.site.register(Person, PersonAdmin)
