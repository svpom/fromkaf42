from django import forms


class UploadImageToEncodeForm(forms.Form):
    img = forms.ImageField(label='Путь к файлу:')
    mes = forms.CharField(label='Секретное сообщение:', max_length=10000,
                          widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))


class UploadImageToDecodeForm(forms.Form):
    img = forms.ImageField(label='Путь к файлу:')
    mes_len = forms.CharField(label='Число символов закодированного сообщения:',
                          max_length=100, widget=forms.TextInput(attrs={'size': '1'}))
