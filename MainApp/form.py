from django import forms
from .models import Article
from django.utils.translation import gettext_lazy as _

class AddArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("__all__")

        CHOICES = [
            ('Please check', 'الرجاء الاختيار '),
            ('news', 'خبر'),
            ('review', 'مراجعة'),
            ('article', 'مقالة'),
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control text-end ', "placeholder":'العنوان'}),
            'article_type': forms.Select(choices=CHOICES,attrs={'class':'form-select text-end ', "placeholder":'العنوان'}),
        }

 