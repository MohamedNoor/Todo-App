from django import forms

class TodoForm (forms.Form):
    text = forms.CharField(max_length=30,
    widget= forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Enter todo e.g. Delete junk files',
            'arial-label' : 'Todo',
            'arial-describedby' : 'addbtn',
        }
    ))