from django.urls import path

from .views import index, chose_category, about, faq


urlpatterns = [
    path('', index, name='home'),
    # path('', HomePageListView.as_view(), name='home'),
    path('category/<slug:cat_slug>/', chose_category, name='category'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
]
