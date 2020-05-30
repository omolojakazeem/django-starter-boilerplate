from django.shortcuts import render


def home_page_view(request):
    template = 'website_app/index.html'
    context = {
        'message': 'Welcome to our website'
    }
    return render(request, template, context=context)
