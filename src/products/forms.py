from django import forms

class ProductAddForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 1.00:
            raise forms.ValidationError("Price must be greater than $1.00")
        elif price >= 99.99:
            raise forms.ValidationError("Price must be less than $100.00")
        return price    

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > 3:
            return title
        else:
            raise forms.ValidationError("Title must be greater than 3 characters long.")    
            