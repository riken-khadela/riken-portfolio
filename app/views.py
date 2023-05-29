from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView
from app.models import project
# Create your views here.

def project_detail(request, slug):
    context = {}
    if project.objects.filter(slug=slug).exists():
        prj = project.objects.get(slug=slug).__dict__
        context['project'] = prj
    else:
        context['project'] = {}
    
    if context['project']['img2'] :
        url1 = context['project']['img2']
        url1 = url1.replace('file/d/','uc?export=view&id=').split('/view')[0]
        context['project']['img2'] = url1
    if context['project']['img3'] :
        url2 = context['project']['img3']
        url2 = url2.replace('file/d/','uc?export=view&id=').split('/view')[0]
        context['project']['img3'] = url2
        
    if 'technologies' in prj :
        if  prj['technologies'] :
            context['project']['technologieslist'] = prj['technologies'].split(',')
            
    if len(project.objects.all()) >=  6:
        
        MoreProjects = []
        for prj in project.objects.order_by('?')[:6]:
            a = {}
            a['title'] = prj.MainTitle
            a['SmallDiscription'] = prj.SmallDiscription
            a['slug'] = prj.slug
            MoreProjects.append(a)
        
        context['project']['more_projects'] = MoreProjects
        print(context['project']['more_projects'],'------------------------')
    return render(request, 'prj_details.html', context)

class project_list(TemplateView):
    template_name = "prj_list.html"
    def get(self, request):
        projects = []
        for prj in project.objects.all():
            a = {}
            a['title'] = prj.MainTitle
            a['SmallDiscription'] = prj.SmallDiscription
            a['slug'] = prj.slug
            projects.append(a)
        context = {
        "data" : projects,
        }
        
        return render(request, self.template_name,context)

def error_404(requests,exception):
    return render(requests,'404.html')

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
