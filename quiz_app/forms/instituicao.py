from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, Button, Div, Field, Layout, Submit)
from django import forms

from ..models import Instituicao

class CadastroInstituicaoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CadastroInstituicaoForm, self).__init__(*args, **kwargs)

    continuar_cadastro = forms.BooleanField(
        label='Após salvar, incluir um novo?',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'custom-control-input'
            }
        )
    )

    
    helper = FormHelper()

    helper.form_class = 'form-group'

    helper.layout = Layout(
        Div(
            Div(
                HTML('<h1 class="pt-3">Cadastro de Instituição</h1>'),
                css_class='row ml-5 mr-5',
            ),
            Div(
                Div(Field('nome_instituicao'), css_class='col-md-6'),
                Div(Field('nome_curso'), css_class='col-md-6'),
                css_class='row',
            ),
            Div(
                FormActions(
                        Div(
                            Div(
                                'continuar_cadastro', css_class='custom-control custom-switch text-right'
                            ),
                            Button('cancel', 'Retornar a consulta', css_class="btn-danger mr-2",
                            onclick='window.location.href="/instituicoes"'),
                            # Button('cancel', 'Encerrar', css_class="btn-warning mr-2",
                            # onclick='window.location.href="/ "'),
                            Submit('save_changes', 'Salvar', css_class="btn-success"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row'
            ),
            css_class="container"
        )
    )

        

    class Meta:
        model = Instituicao
        fields = ('__all__')