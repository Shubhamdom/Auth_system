'''from django import forms
from .models import category,subcategory


class category(forms.ModelForm):
    class Meta:
        model=category
        fields=('category')

class subcategory(forms.ModelForm):
    class Meta:
        model=subcategory
        fields ={"category","subcategory"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = category.objects.none()'''