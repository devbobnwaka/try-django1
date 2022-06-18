from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    #cleaning only one data
    def clean_title(self):
        cleaned_data = self.cleaned_data #dictionary
        print("cleaned_data" , cleaned_data)
        title = cleaned_data.get('title')
        if title.lower().strip() == "the office":
            raise forms.ValidationError('This is taken.')
        print("title" , title)
        return title

    #to clean all data
    def clean(self):
        cleaned_data = self.cleaned_data #dictionary
        print("all_data" , cleaned_data)
        return cleaned_data