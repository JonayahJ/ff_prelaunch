from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def dynamic_pages(request, page):
    page_text = None
    if page == "home":
        page_text = "This works!"
    elif page == "survey":
        page_text = "This is the questionnaire!"
    else:
        return HttpResponseNotFound("This page is not supported.")
    return HttpResponse(page_text)