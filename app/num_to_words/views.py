import json
import os

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from utils.utils import number_is_supported, number_to_english, MAX_NUMBER_SUPPORTED


def index():
   return HttpResponse("Index")


class num2EnglishView(View):
    def post(self, request):
        data = {}
        data['status'] = 'NOK'
        json_data = json.loads(request.body)

        try:
            number_string = json_data['number']
            number = int(number_string)
        except KeyError:
            data['error'] = 'number param is not present'
        except ValueError:
            data['error'] = 'The param provided is not a number'

        if 'error' in data:
            return JsonResponse(data)

        if number_is_supported(number):
            data['status'] = 'OK'
            data['num_in_english'] = number_to_english(number)
        else:
            data['error'] = f'Number {number} is not supported. It must be less than {MAX_NUMBER_SUPPORTED}'

        return JsonResponse(data)

    def get(self, request):
        data = {}
        data['status'] = 'NOK'
        number_string = request.GET.get('number', None)
 
        if number_string == None or not number_string.isnumeric():
            data['error'] = 'number param is not present or is not valid'
            return JsonResponse(data)

        number = int(number_string)
        if number_is_supported(number):
            data['status'] = 'OK',
            data['num_in_english'] = number_to_english(number),
        else:
            data['error'] = f'Number {number} is not supported. It must be less than {MAX_NUMBER_SUPPORTED}'

        return JsonResponse(data)
