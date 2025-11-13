from django import template
from django.urls import reverse
from django.utils.text import slugify

from tree.models import Menu, MenuItem

register = template.Library()


class MenuTreeRenderer:
    def __init__(self, menu: Menu, request_path: str) -> None:
        self.menu = menu
        self.current_segments = self._extract_segments(request_path)

    def render(self) -> str:
        top_items = self.menu.items.filter(parent__isnull=True)
        return self._render_items(top_items, [])

    def _render_items(self, items, parent_segments) -> str:
        parts = ['<ul>']
        for item in items:
            segments = parent_segments + [self._slug(item)]
            parts.append(self._render_item(item, segments))
        parts.append('</ul>')
        return ''.join(parts)

    def _render_item(self, item: MenuItem, segments) -> str:
        parts = [f'<li><a href="{self._url_for(segments)}">{self._title_for(item, segments)}</a>']
        children = item.children.all()
        if children and self._is_expanded(segments):
            parts.append(self._render_items(children, segments))
        parts.append('</li>')
        return ''.join(parts)

    def _title_for(self, item: MenuItem, segments) -> str:
        return f'<strong>{item.name}</strong>' if self._is_active(segments) else item.name

    def _slug(self, item: MenuItem) -> str:
        return slugify(item.name) or str(item.pk)

    def _url_for(self, segments) -> str:
        return reverse('menu_item', kwargs={'menu_path': '/'.join(segments)})

    def _is_active(self, segments) -> bool:
        return segments == self.current_segments

    def _is_expanded(self, segments) -> bool:
        return self._is_active(segments) or self.current_segments[:len(segments)] == segments

    @staticmethod
    def _extract_segments(path: str):
        parts = [p for p in path.strip('/').split('/') if p]
        return parts[1:] if len(parts) > 1 else []


@register.inclusion_tag('menu.html', takes_context=True)
def main_menu(context: dict, menu_name: str) -> dict:
    menu = Menu.objects.prefetch_related('items__children').get(name=menu_name)
    request = context['request']
    renderer = MenuTreeRenderer(menu, request.path)
    return {"menu": menu, "menu_html": renderer.render()}
