from django.shortcuts import render
from django.http import Http404 ,HttpResponseRedirect
from .models import Notes
from django.views.generic import CreateView, DetailView, ListView , UpdateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NotesForm

# Create your views here.


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/log"


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/log"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    # template_name = "TEMPLATE_NAME"


class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = "notes/notes_list.html"
    login_url = "/log"

    def get_queryset(self):
        return self.request.user.notes.all()

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request,'notes/notes_list.html' ,{'notes':all_notes} )


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.html'


# def detail(request,pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404('notes does not exist')
#     return render(request,'notes/notes_detail.html',{'note': note})