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

def custom_404_view(request, exception):
    """
    Custom 404 error handler for Django.
    Renders the 404.html template.
    """
    return render(request, 'Templates/404.html', status=404)

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
class like_me_fast(TemplateView):
    template_name = "prt/like_me_fast.html"
    def get(self, request):
        return render(request, self.template_name)

# --------------------------------------------------------------2
class CoinHomes(TemplateView):
    template_name = "prt/CoinHomes.html"
    def get(self, request):
        return render(request, self.template_name)    

    
# --------------------------------------------------------------3
class Pharsight(TemplateView):
    template_name = "prt/Pharsight.html"
    def get(self, request):

        return render(request, self.template_name) 
       
# --------------------------------------------------------------4
class ShreeTextTile(TemplateView):
    template_name = "prt/ShreeTextTile.html"
    def get(self, request):

        return render(request, self.template_name)    
        
# --------------------------------------------------------------5
class Instagram(TemplateView):
    template_name = "prt/Instagram.html"
    def get(self, request):
        return render(request, self.template_name)    

# --------------------------------------------------------------6
class dyzner(TemplateView):
    template_name = "prt/dyzner.html"
    def get(self, request):
        return render(request, self.template_name)    

# --------------------------------------------------------------7
class Hallour(TemplateView):
    template_name = "prt/Hallour.html"
    def get(self, request):
        return render(request, self.template_name)    
# --------------------------------------------------------------7
class domainmarket(TemplateView):
    template_name = "prt/domain_market.html"
    def get(self, request):
        return render(request, self.template_name)    
# --------------------------------------------------------------7
class YouTube(TemplateView):
    template_name = "prt/youtube.html"
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
