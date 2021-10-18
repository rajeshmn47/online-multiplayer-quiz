from django.contrib import admin
from .models import *

# Register your models here.
class questionsadmin(admin.ModelAdmin):
    list_display=('question_text','option1','option2','option3','option4','answer')

admin.site.register(questions,questionsadmin)

class scoreadmin(admin.ModelAdmin):
    list_display=('scores','user')

admin.site.register(score,scoreadmin)

