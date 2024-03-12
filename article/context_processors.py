from .models import Category, Article



def cat(request):
    context = {
        'categories': Category.objects.select_related('parent').prefetch_related('articles')\
            .filter(is_parent = True, status = True)
    }
    return context


def art(request):
    context = {
        'articles': Article.objects.filter(status = 'P')
    }
    return context
