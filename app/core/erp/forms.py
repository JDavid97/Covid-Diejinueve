from django.forms import *
from core.erp.models import Paciente, Doctor

class PacienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombres': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nro_documento': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'celular': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'fecha_registro': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'genero': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),            
        }
        

class DoctorForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'nombres': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'apellidos': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nro_documento': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nro_celular': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'genero': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'especialidad': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ), 
        }