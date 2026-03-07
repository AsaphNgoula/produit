from django.shortcuts import redirect, render,get_object_or_404
from django.views import View
from .models import Courses
from .forms import CourseForm

# Create your views here.
class List_View(View):
    template_name='courses/courses_list.html'
    def get(self, request,*args, **kwargs):
        queryset=Courses.objects.all()
        return render(request, self.template_name, {'object_list':queryset})


class Detail_View(View):
    template_name='courses/courses-detail.html'
    def get(self,request,*args,id=None, **kwargs):
        id =self.kwargs.get('pk')
        context={}
        if id is not None:
            obj=get_object_or_404(Courses,id=id)
            context['object']=obj
            return render(request,self.template_name,context)
        
class Create_View(View):
    form_class=CourseForm()
    template_name='courses/courses-create.html'
    def get(self,request,*args, **kwargs):
        return render(request, self.template_name,{'form':self.form_class})
    
    def post(self,request,*args, **kwargs):
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/courses')
        return render(request, self.template_name, {'form': form})
