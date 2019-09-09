from django import template
from datetime import datetime
from datetime import timedelta

register = template.Library()


@register.filter
def format_date(value):

    formated_date = datetime.fromtimestamp(int(value))
    now = datetime.now()
    delta = now - formated_date
    if delta.seconds <= 600:
        post_date = 'Только что'
    elif delta.seconds <= 86400:
        post_date = f'{int(delta.seconds / 60 / 60)} часов назад'
    else:
        post_date = formated_date
    return post_date

@register.filter
def format_score(value):
    if value <= -5:
        rate = 'Очень низкий рейтинг'
    elif value <= 5:
        rate = 'Средний рейтинг'
    elif value > 5:
        rate = 'Высокий рейтинг'
    else:
        rate = value
    return rate
# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    if value == 0:
        comments = 'Оставьте комментарий'
    elif value >= 0 and value < 50:
        comments = value
    elif value >= 50:
        comments = '50+'
    return comments

@register.filter
def format_selftext(value, count):
    value = value.split(' ')
    if len(value) < count * 2:
        description = 'Thers is no article description...'
    else:
        description =  ' '.join(value[:count]) + '...' + ' '.join(value[-count:])

    return description
