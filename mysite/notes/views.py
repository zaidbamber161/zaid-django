from django.http import HttpResponse
from notes.models import MyNotes
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from notes.forms import NoteForm


def addnote(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        error = None
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('viewnotes'))
        else:
            return render(request, 'notes/addnote.html', {'form': form, 'error': error})
    else:
        form = NoteForm()
    return render(request, 'notes/addnote.html', {'form': form, })


def onDeleteStatus(request, pk):
    data = MyNotes.objects.get(id=pk)
    data.is_active = False
    data.save()
    return HttpResponseRedirect(reverse('viewnotes'))


def onReadStatus(request, pk):
    data = MyNotes.objects.get(id=pk)
    data.is_read = True
    data.save()
    return HttpResponseRedirect(reverse('viewnotes'))


class ListNotes(ListView):
    template_name = 'notes/viewnotes.html'
    context_object_name = 'notes_list'

    def get_queryset(self):
        return MyNotes.objects.filter(is_active='True')


class UpdateNotes(UpdateView):
    model = MyNotes
    template_name = 'notes/updatenote.html'
    fields = ['title', 'description', 'note_created_date']

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('viewnotes'))
