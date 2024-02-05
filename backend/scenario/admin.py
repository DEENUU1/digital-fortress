from django.contrib import admin
from .models import Project, Scenario


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'storage_usage', 'num_of_scenarios', 'user')
    list_filter = ('user',)
    search_fields = ('title',)


class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('project', 'parent_id', 'user')
    list_filter = ('user',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Scenario, ScenarioAdmin)
