from django import forms
from django.contrib.auth import get_user_model
# from django_select2.forms import HeavySelect2Widget
from django_select2.forms import ModelSelect2Widget
from .models import Liquidacion
from django.urls import reverse_lazy


User = get_user_model()


class UsuarioSelectWidget(ModelSelect2Widget):
    model = User
    search_fields = [
        "identidad__icontains",
        "first_name__icontains",
        "last_name__icontains",
    ]

    def get_url(self):
        return reverse_lazy('liquidaciones:usuario-autocomplete')

    def label_from_instance(self, obj):
        return f"{obj.identidad} - {obj.first_name} {obj.last_name}"


class LiquidacionForm(forms.ModelForm):
    tecnico = forms.ModelChoiceField(
        queryset=User.objects.filter(is_active=True),
        widget=forms.Select(
            attrs={
                'class': 'w-full rounded-xl border-gray-300 px-4 py-2 shadow-sm focus:ring-2 focus:ring-green-500'
            }
        ),
        label="Técnicos"
    )

    class Meta:
        model = Liquidacion
        fields = '__all__'
        widgets = {
            'mes': forms.TextInput(attrs={
                'class': 'w-full border-gray-300 rounded-xl px-4 py-2 shadow-sm focus:ring-2 focus:ring-green-500',
                'placeholder': 'Ej. Numero de Mes'
            }),
            'año': forms.TextInput(attrs={
                'class': 'w-full border-gray-300 rounded-xl px-4 py-2 shadow-sm focus:ring-2 focus:ring-green-500',
                'placeholder': 'Ej. 2025'
            }),
            'monto': forms.NumberInput(attrs={
                'class': 'w-full border-gray-300 rounded-xl px-4 py-2 shadow-sm focus:ring-2 focus:ring-green-500',
                'placeholder': 'Ej. 1000000'
            }),
            'archivo_pdf_liquidacion': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-green-50 file:text-green-700 hover:file:bg-green-100',
                'accept': 'application/pdf',
                'required': True
            }),
            'pdf_firmado': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100',
                'accept': 'application/pdf'
            }),
            'fecha_firma': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'w-full border-gray-300 rounded-xl px-4 py-2 shadow-sm focus:ring-2 focus:ring-green-500'
            }),
            'firmada': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 text-green-600'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # ✅ Validación en el navegador
        self.fields['monto'].required = True
        self.fields['monto'].widget.attrs['required'] = 'required'

    def clean_tecnico(self):
        tecnico = self.cleaned_data.get('tecnico')
        if self.request:
            usuario = self.request.user
            if hasattr(usuario, 'tecnico') and tecnico != usuario.tecnico:
                raise forms.ValidationError(
                    "No puedes crear liquidación para otro técnico."
                )
        return tecnico

    def clean_archivo_pdf_liquidacion(self):
        archivo = self.cleaned_data.get('archivo_pdf_liquidacion')
        if not archivo:
            raise forms.ValidationError("Debes adjuntar un archivo PDF.")
        return archivo

    def clean_monto(self):
        monto = self.cleaned_data.get('monto')
        if monto is None:
            raise forms.ValidationError("Debes ingresar un monto.")
        return monto
