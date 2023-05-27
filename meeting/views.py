from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Language

from django.views.generic import ListView


menu = [
    {'title': 'language loop', 'url_name': 'home'},
    {'title': 'about', 'url_name': 'about'},
    {'title': 'faq', 'url_name': 'faq'},
]


def index(request):
    meetings_list = Post.objects.all()
    languages = Language.objects.annotate(total=Count('post')).filter(total__gt=0)
    
    paginator = Paginator(meetings_list, 2)
    page_number = request.GET.get('page', 1)

    try:
        meetings = paginator.page(page_number)
        # obtain the objects for the desired page by calling the page() method of Paginator
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        meetings = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        meetings = paginator.page(paginator.num_pages)

    context = {
        'title': 'meetings',
        'meetings': meetings,
        'languages': languages,
        'menu': menu,
    }
    return render(request, template_name='meeting/index.html', context=context)


def chose_category(request, cat_slug):
    meetings = Post.objects.filter(language__slug=cat_slug)
    languages = Language.objects.annotate(total=Count('post')).filter(total__gt=0)
    context = {
        'title': 'meetings',
        'meetings': meetings,
        'languages': languages,
        'menu': menu,
    }
    return render(request, template_name='meeting/index.html', context=context)


def about(request):
    context = {
        'title': 'about',
        'menu': menu,
    }
    return render(request, template_name='meeting/about.html', context=context)


def faq(request):
    context = {
        'title': 'faq',
        'menu': menu,
    }
    return render(request, template_name='meeting/faq.html', context=context)


# class HomePageListView(ListView):
#     model = Post
#     template_name = 'meeting/index.html'
#     context_object_name = 'meetings'
#
#     # def get_queryset(self):
#     #     return Post.objects.all()
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'meetings'
#         context['languages'] = Language.objects.all()
#         context['meetings'] = Post.objects.all()
#         context['menu'] = menu


# class MeetingHome(ListView):
#     model = Post
#     template_name = 'meeting/index.html'
#     context_object_name = 'meetings'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'meetings'
#         context['menu'] = menu
#         return context
