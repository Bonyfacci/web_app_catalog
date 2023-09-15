from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from catalog.models import Product, News, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_created'].widget = AdminDateWidget(attrs={'type': 'date'})
        self.fields['date_updated'].widget = AdminDateWidget(attrs={'type': 'date'})

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('owner',)

    def clean_name(self):
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['name']
        for i in word_list:
            if i in cleaned_data:
                raise forms.ValidationError(f"Нельзя использовать в названии и описании такие слова, как: "
                                            f"{' '.join(word_list)}")

        return cleaned_data

    def clean_description(self):
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['description']
        for i in word_list:
            if i in cleaned_data:
                raise forms.ValidationError(f"Нельзя использовать в названии и описании такие слова, как: "
                                            f"{' '.join(word_list)}")

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['current_version'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:
        model = Version
        fields = '__all__'


class NewsForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'
