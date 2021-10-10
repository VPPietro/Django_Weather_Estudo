from django.http.response import HttpResponseBase
from django.http import HttpRequest
from django.views.generic import FormView

from apps.city_app.forms import SearchForm


class HomePage(FormView):
    template_name = 'main.html'
    form_class = SearchForm

    # def dispatch(self, request: HttpRequest, *args: any, **kwargs: any) -> HttpResponseBase:
    #     # print(request.POST)
    #     return super().dispatch(request, *args, **kwargs)
