from django import template

register = template.Library()


@register.filter(name="next_img")
def next_img(current_img, total):
    if current_img >= total:
        return f'#img-{1}'
    return f'#img-{current_img + 1}'


@register.filter(name="previous_img")
def previous_img(current_img, total):
    if current_img <= 1: 
        return f'#img-{total}'
    return f'#img-{current_img - 1}'


@register.filter(name="active_grid")
def active_grid(grid, button):
    if grid == button:
        return 'active'
    else:
        return 