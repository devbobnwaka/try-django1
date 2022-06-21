from turtle import title
from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data['title']
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"\"{title}\" is already in use. Pick another title")
        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    #cleaning only one data
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data #dictionary
    #     print("cleaned_data" , cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError('This is taken.')
    #     print("title" , title)
    #     return title

    #to clean all data
    def clean(self):
        cleaned_data = self.cleaned_data #dictionary
        print("all_data" , cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "the office":
            self.add_error('title', 'the office')
            # raise forms.ValidationError('This is taken.')
        if "office" in content or "office" in title.lower():
            self.add_error('content', "Office cannot be in content")
            raise forms.ValidationError('Office is not allowed')
        return cleaned_data