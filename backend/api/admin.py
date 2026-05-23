from django.contrib import admin
from .models import Application
from .models import Intern #for intern


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'role',
        'duration',
        'college',
        'status',         
        'applied_at',
    )

    list_filter = (
        'status',       
        'role',
        'duration',
        'applied_at',
    )

    search_fields = ('name', 'email', 'college')
    ordering = ('-applied_at',)

    #intern data 

@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "course",
        "internship_field",
        "duration",
        "start_date",
        "end_date",
    )

    search_fields = (
        "name",
        "email",
        "course",
    )
