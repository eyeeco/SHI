from django.views.generic import RedirectView, TemplateView


class IndexView(TemplateView):
    """
    A index view.
    """
    template_name = 'base/layout.html'
