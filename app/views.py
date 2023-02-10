from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect

# Create your views here.

class Home(TemplateView):
    template_name = "index.html"
    def get(self, request):
        
        return render(request, self.template_name)
    
    def post(self,request):
        return render(request,self.template_name)

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
    
# --------------------------------------------------------------1
class prt1(TemplateView):
    template_name = "prt/1.html"
    def get(self, request):
        return render(request, self.template_name)

# --------------------------------------------------------------2
class prt2(TemplateView):
    template_name = "prt/2.html"
    def get(self, request):
        return render(request, self.template_name)    

    
# --------------------------------------------------------------3
class prt3(TemplateView):
    template_name = "prt/3.html"
    def get(self, request):

        return render(request, self.template_name) 
       
# --------------------------------------------------------------4
class prt4(TemplateView):
    template_name = "prt/4.html"
    def get(self, request):

        return render(request, self.template_name)    
        
# --------------------------------------------------------------5
class prt5(TemplateView):
    template_name = "prt/5.html"
    def get(self, request):
        return render(request, self.template_name)    

# --------------------------------------------------------------6
class prt6(TemplateView):
    template_name = "prt/6.html"
    def get(self, request):
        return render(request, self.template_name)    

# --------------------------------------------------------------7
class prt7(TemplateView):
    template_name = "prt/7.html"
    def get(self, request):
        return render(request, self.template_name)    

# --------------------------------------------------------------8
class prt8(TemplateView):
    template_name = "prt/8.html"
    def get(self, request):
        return render(request, self.template_name)    

# --------------------------------------------------------------9
class prt9(TemplateView):
    template_name = "prt/9.html"
    def get(self, request):
        return render(request, self.template_name)    

# --------------------------------------------------------------10
class prt10(TemplateView):
    template_name = "prt/10.html"
    def get(self, request):
        return render(request, self.template_name)
