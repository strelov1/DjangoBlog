from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import resolve_url
from .forms import ArticleForm
from .models import Article


class ArticleCreate(CreateView):
    model = Article
    template_name = 'create.html'
    fields = ('title', 'text')

    def get_success_url(self):
        return resolve_url('detail', pk=self.object.pk)


class ArticleUpdate(UpdateView):
    model = Article
    template_name = 'update.html'
    fields = ('title', 'text')

    def get_success_url(self):
        return resolve_url('detail', pk=self.object.pk)


class ArticleIndex(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'list.html'

    def dispatch(self, request, *args, **kwargs):
        self.form = ArticleForm(request.GET)
        self.form.is_valid()
        return super(ArticleIndex, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ArticleIndex, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'detail.html'
