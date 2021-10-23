from django import template

register = template.Library()

@register.filter
def duration(seconds):
    """Takes in a integer of seconds and formats it to hours"""
    hours = round(seconds / 3600)
    return f"{hours} {'hour' if hours == 1 else 'hours'}"