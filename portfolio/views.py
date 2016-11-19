from django.views import generic

from .models import Page


class IndexView(generic.TemplateView):
    template_name = 'portfolio/index.html'
    active = 'index'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['active'] = self.active
        return context


class PortfolioView(generic.TemplateView):
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'page'


class ProjectsView(generic.TemplateView):
    template_name = 'portfolio/projects.html'
    active = 'projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectsView, self).get_context_data(**kwargs)
        context['active'] = self.active
        return context


class ContactView(generic.TemplateView):
    template_name = 'portfolio/contact.html'
    active = 'contact'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['active'] = self.active
        return context
