from django import forms

class DateForm(forms.Form):
    from_date = forms.DateInput(label="from date")
    to_date = forms.DateInput(label="to date")