from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect

# Create your views here.

class Home(TemplateView):
    template_name = "index.html"
    def get(self, request):

        return render(request, self.template_name)

class about_us(TemplateView):
    template_name = "about-us.html"
    def get(self, request):

        return render(request, self.template_name)

class blog(TemplateView):
    template_name = "blog.html"
    def get(self, request):

        return render(request, self.template_name)

class contact(TemplateView):
    template_name = "contact.html"
    def get(self, request):

        return render(request, self.template_name)

class elements(TemplateView):
    template_name = "elements.html"
    def get(self, request):

        return render(request, self.template_name)

class portfolio(TemplateView):
    template_name = "portfolio.html"
    def get(self, request):

        return render(request, self.template_name)

class services(TemplateView):
    template_name = "services.html"
    def get(self, request):

        return render(request, self.template_name)

class single_blog(TemplateView):
    template_name = "single-blog.html"
    def get(self, request):

        return render(request, self.template_name)