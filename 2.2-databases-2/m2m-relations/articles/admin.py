from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope

class ScopeipInline(admin.TabularInline):
    model = Scope
class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):

        if len(self.forms) == 0:
            raise ValidationError('Не указаны теги!')

        self.count_is_main_tag = 0

        for form in self.forms:
            if self.count_is_main_tag > 0 and form.cleaned_data.get('is_main'):
                raise ValidationError('Главный может быть только 1 тег')
            else:
                if form.cleaned_data.get('is_main'):
                    print(f"{form.cleaned_data.get('tag')} - главный раздел")
                    self.count_is_main_tag += 1
                else:
                    continue

        return super().clean()



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeipInline]
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


