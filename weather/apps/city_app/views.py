from django.http.response import HttpResponseBase
from django.http import HttpRequest
from django.views.generic import FormView
import requests
import json

from apps.city_app.forms import SearchForm


class HomePage(FormView):
    template_name = 'home.html'
    form_class = SearchForm
    extra_context = {}

    def dispatch(self, request: HttpRequest, *args: any, **kwargs: any) -> HttpResponseBase:
        self.city_search = request.GET.get('city_search')
        if self.city_search:
            request.session['city_search'] = self.city_search
        else:
            if request.session.get('city_search'):
                del request.session['city_search']
                self.extra_context = {}
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: any) -> dict:
        if self.city_search:
            request_api = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={self.city_search}&appid=dfeaeea289e0fe52448221942b1e1f8f&units=metric&lang=pt_br')
            request_api = json.loads(request_api.content.decode('utf-8'))
            if request_api['cod'] == 200:
                self.extra_context['weatherapi_result'] = request_api
                self.extra_context['timezone'] = (request_api['timezone'] / 60) / 60
            else:
                self.extra_context['weatherapi_result'] = 'not_found'
        return super().get_context_data(**kwargs)
