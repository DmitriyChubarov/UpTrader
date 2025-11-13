from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = 'test_menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_path'] = kwargs.get('menu_path')
        return context