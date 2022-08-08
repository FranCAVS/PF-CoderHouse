from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Page
from .forms import PageForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class StaffRequiredMixin(object):
    """ Este mixin requerirá que el usuario sea miembro del staff """
@method_decorator(staff_member_required)
def dispatch(self, request, *args, **kwargs):
     return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


@login_required
def dummy(request):
    render(request, "")


# Create your views here.
class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page


class PageCreate(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PageUpdate(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
            return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageDelete(LoginRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    permission_required = ("pages.delete_Page")


def buscar(request):
    if request.GET['title']:
        title= request.GET['title']
        pages = Page.objects.filter(title__icontains=title)
        return render(request, 'page_results.html', {'pages':pages, 'title':title})
    else:
        base = 'page_error_not_find.html'
    return render(request, base, {})


def about(request):
    return render(request, 'page_about.html')