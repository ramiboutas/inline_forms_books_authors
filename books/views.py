from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect

from books.models import Book, Author
from books.forms import AuthorBooksFormSet


class HomeView(TemplateView):
    template_name = 'home.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'authors.html'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'create_author.html'
    fields = ['name', ]

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'The author has been created')
        return super().form_valid(form)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'view_author.html'


class AuthorBooksUpdateView(SingleObjectMixin, FormView):
    model = Author
    template_name = 'update_authorbooks.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all()) # method of SingleObjectMixin
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all()) # method of SingleObjectMixin
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return AuthorBooksFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Changes were save')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('books:view_author', kwargs={'pk':self.object.pk})
