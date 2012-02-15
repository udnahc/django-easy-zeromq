from django import forms

class CreateSocketForm(forms.Form):
    socket_name = forms.CharField(required=True, widget=forms.TextInput())
    port = forms.CharField(required=True, widget=forms.TextInput())
    socket_type = forms.ChoiceField(required=True, choices = [('PULL','zmq.PULL'), ('PUSH', 'zmq.PUSH'), ('PUB','zmq.PUB'), ('SUB','zmq.SUB')], label='Socket Type')
    description = forms.CharField(required=True, widget=forms.TextInput())
    python_package = forms.CharField(required=True, widget=forms.TextInput())
