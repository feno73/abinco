from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class FormularioCreacionUsuario(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioCreacionUsuario, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


class FormularioInicioSesion(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioInicioSesion, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password']:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})