from math import floor
from django import template
from django.utils.encoding import force_text
import re

register = template.Library()


@register.inclusion_tag('zui/pagination.html')
def zui_pagination(page, **kwargs):
    """
    Render pagination for a page

    **Tag name**::

        bootstrap_pagination

    **Parameters**:

        :page:
        :kwargs:

    **usage**::

        {% bootstrap_pagination FIXTHIS %}

    **example**::

        {% bootstrap_pagination FIXTHIS %}
    """

    pagination_kwargs = kwargs.copy()
    pagination_kwargs['page'] = page
    return get_pagination_context(**pagination_kwargs)


def get_pagination_context(page, pages_to_show=11,
                           url=None, style=None, extra=None):
    """
    Generate Bootstrap pagination context from a page object
    """
    pages_to_show = int(pages_to_show)
    if pages_to_show < 1:
        raise ValueError("Pagination pages_to_show should be a positive " +
                         "integer, you specified {pages}".format(pages=pages_to_show))
    num_pages = page.paginator.num_pages
    current_page = page.number
    half_page_num = int(floor(pages_to_show / 2)) - 1
    if half_page_num < 0:
        half_page_num = 0
    first_page = current_page - half_page_num
    if first_page <= 1:
        first_page = 1
    if first_page > 1:
        pages_back = first_page - half_page_num
        if pages_back < 1:
            pages_back = 1
    else:
        pages_back = None
    last_page = first_page + pages_to_show - 1
    if pages_back is None:
        last_page += 1
    if last_page > num_pages:
        last_page = num_pages
    if last_page < num_pages:
        pages_forward = last_page + half_page_num
        if pages_forward > num_pages:
            pages_forward = num_pages
    else:
        pages_forward = None
        if first_page > 1:
            first_page -= 1
        if pages_back is not None and pages_back > 1:
            pages_back -= 1
        else:
            pages_back = None
    pages_shown = []
    for i in range(first_page, last_page + 1):
        pages_shown.append(i)
        # Append proper character to url
    if url:
        # Remove existing page GET parameters
        url = force_text(url)
        url = re.sub(r'\?page\=[^\&]+', '?', url)
        url = re.sub(r'\&page\=[^\&]+', '', url)
        # Append proper separator
        if '?' in url:
            url += '&'
        else:
            url += '?'
            # Append extra string to url
    if extra:
        if not url:
            url = '?'
        url += force_text(extra) + '&'
    if url:
        url = url.replace('?&', '?')
    # Set CSS classes, see http://getbootstrap.com/components/#pagination
    pagination_css_classes = ['pager']
    if style == 'pills':
        pagination_css_classes.append('pager-pills')
    elif style == 'loose':
        pagination_css_classes.append('pager-loose')
    elif style == 'justify':
        pagination_css_classes.append('pager-justify')
        # Build context object
    return {
        'zui_pagination_url': url,
        'num_pages': num_pages,
        'current_page': current_page,
        'first_page': first_page,
        'last_page': last_page,
        'pages_shown': pages_shown,
        'pages_back': pages_back,
        'pages_forward': pages_forward,
        'pagination_css_classes': ' '.join(pagination_css_classes),
    }
