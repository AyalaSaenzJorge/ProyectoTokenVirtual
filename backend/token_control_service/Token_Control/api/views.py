from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Tokens
import json
import requests
import time 


# Create your views here.

class TokensView(View):

    def get(self, request):
        customer = request.GET['cliente']
        tokenCreationServiceURL = 'http://127.0.0.1:8001/crear_token'
        tokenCreationServiceParams = {'cliente':customer}

        tokens = list(Tokens.objects.filter(username=customer).order_by('-id').values())

        if len(tokens) >= 1:
            token = tokens[0]
            # Validate the current token
            currentTime = time.time_ns()
            validationFactor = currentTime - token['created_since']
            isValid =  validationFactor in range(0, 60000000000)
        
            if isValid:
                #Update the timesUsed in DB
                newToken = Tokens.objects.get(id=token['id'])
                newToken.times_used = token['times_used'] + 1
                newToken.save()
                token['times_used'] = newToken.times_used
                # Return the token info
                secondsLeft = 60 - int(validationFactor / 1000000000)
                answer = {'status': 200, 'message' : 'Token válido', "username": customer, 'token': token['token_value'], 'secondsLeft': secondsLeft}
            else:
                #Create new random token from the other service
                try:
                    tokenCreationResponse = requests.get(url = tokenCreationServiceURL, params = tokenCreationServiceParams)
                    serviceResponse = tokenCreationResponse.json()
                
                    if serviceResponse['status'] == 200:
                        tokenTime = time.time_ns()
                        newToken = serviceResponse['token']
                        Tokens.objects.create(username=customer, token_value=newToken, created_since=tokenTime, times_used = 1)
                        answer = {'status': 200, 'message' : 'Nuevo token generado.', "username": customer, 'token': newToken, 'secondsLeft': 60}
                    else:
                        answer = {'status': 500, 'message' : 'Falló servicio de generación de nuevo token'}
                except:
                    answer = {'status': 500, 'message' : 'Token expirado, pero no se puede generar nuevo token porque el servicio no está disponible', "username": customer, 'token': token['token_value'], 'secondsLeft': 0}
                
        else:
            try:
                #Create new random token from the other service
                tokenCreationResponse = requests.get(url = tokenCreationServiceURL, params = tokenCreationServiceParams)
                serviceResponse = tokenCreationResponse.json()
                if serviceResponse['status'] == 200:
                    tokenTime = time.time_ns()
                    newToken = serviceResponse['token']
                    Tokens.objects.create(username=customer, token_value=newToken, created_since=tokenTime, times_used = 1)
                    answer = {'status': 200, 'message' : 'Nuevo token generado.', "username": customer, 'token': newToken, 'secondsLeft': 60}
                else:
                    answer = {'status': 500, 'message' : 'Falló servicio de generación de nuevo token'}
            except:
                answer = {'status': 500, 'message' : 'No se puede generar nuevo token porque el servicio no está disponible'}

        return JsonResponse(answer)

class TokenValidationView(View):

    def get(self, request):
        customer = request.GET['cliente']
        tokenValue = request.GET['token']

        tokens = list(Tokens.objects.filter(username=customer, token_value=tokenValue).order_by('-id').values())
    
        if len(tokens) > 0:
            token = tokens[0]
            # Validate the current token
            currentTime = time.time_ns()
            validationFactor = currentTime - token['created_since']
            isValid =  validationFactor in range(0, 60000000000)
            secondsLeft = 60 - int(validationFactor / 1000000000)
            tokenUsage = token['times_used']    
            answer = {'status': 200, 'message' : 'Token existente', 'isValid': isValid, 'secondsLeft': secondsLeft, 'timesUsed' : tokenUsage}
        else:
            #Token not found
            answer = {'status': 400, 'message' : 'Token no existente', 'isValid': False}

        return JsonResponse(answer)

    