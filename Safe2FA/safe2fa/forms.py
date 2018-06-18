from django import forms

OPERATIONS=[
    ("transfer_id", "Transfer money to another account"),
    ("delete_id", "Delete account"),
    ("change_phone_id", "Change phone number")
]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ChooseForm(forms.Form):
    widget = forms.ChoiceField(label='Choose operation: ', choices=OPERATIONS)