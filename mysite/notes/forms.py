from django.forms import ModelForm, forms
from notes.models import MyNotes


class NoteForm(ModelForm):
    class Meta:
        model = MyNotes
        fields = '__all__'