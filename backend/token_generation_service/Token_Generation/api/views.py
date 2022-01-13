from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
import random

# Create your views here.
class TokenGenerationView(View):

    def get(self, request):
        customer = request.GET['cliente']

        tokenValue = random.randrange(111111, 999999)

        answer = {'status': 200, 'cliente': customer, 'token': tokenValue, 'message' : 'Token generado'}

        return JsonResponse(answer)
