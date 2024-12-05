from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.core.cache import cache
from django.views.decorators.cache import cache_page
import time
from .tasks import sendEmail
import requests

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")
@cache_page(60)
def test(request):
    response = requests.get("https://a99d8b73-4245-4719-910a-0eafe72d7cd1.mock.pstmn.io/test/delay/5/")
    return JsonResponse(response.json())