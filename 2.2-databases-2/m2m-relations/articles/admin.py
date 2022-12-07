from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_main = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            #form.cleaned_data
            if form.cleaned_data['is_main'] == True:
                count_main += 1
            if count_main > 1:
                break
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
        if count_main == 0:    
            raise ValidationError('Не указан основной тег')
        elif count_main > 1:
            raise ValidationError('Указано больше одного основного тега')

        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','published_at']
    inlines = [ScopeInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
