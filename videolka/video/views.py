from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def video_page(request:HttpRequest) -> HttpResponse:
    return HttpResponse('This is video')
