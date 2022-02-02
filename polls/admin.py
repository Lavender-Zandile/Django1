from django.contrib import admin

#to create a functionality to add question from the admin

from .models import Question, Choice #bringing in the models
#to change the site header and title
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields':['pub_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInline]
#admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)

