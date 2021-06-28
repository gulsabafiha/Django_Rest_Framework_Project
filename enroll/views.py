from django.views.generic.base import RedirectView, TemplateView, View
from enroll.forms import StudentRegistration
from django.shortcuts import redirect, render,HttpResponseRedirect
from .models import User


class UserAddShow(TemplateView):
    template_name='enroll/addandshow.html'
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        fm=StudentRegistration()
        stu=User.objects.all()
        context={'stu':stu,'form':fm}
        return context
    def post(self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
               
class UserDelete(RedirectView):
    url='/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

class UpdateView(View):
    def get(self,request,id):
       pi=User.objects.get(pk=id)
       fm=StudentRegistration(instance=pi)
       return render(request,'enroll/update.html',{'form':fm})

    def post(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/")


        