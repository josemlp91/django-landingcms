from django.shortcuts import render
from django.shortcuts import get_object_or_404

from content.models import  FieldContent
from content.content_manager import CMSContentManager

from content.forms import  TitleContentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from cms.models import Menu, Configuracion, PaginaHome
import sys

def login_view(request):
    logout(request)
    username = password = ''
    context = dict()

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

    return render(request, 'login.html', context=context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



def home(request):
    #config = Configuracion.objects.all()[0]
    menu = Menu.objects.all()

    try:
        pagina_home = PaginaHome.objects.all()[0]
    except:
        pagina_home = PaginaHome()
        pagina_home.save()

    context = dict()
    #context['config'] = config
    context['menu'] = menu
    context['pagina_home'] = pagina_home
    return render(request, 'home.html', context=context)


def home_cms_edit(request, fieldtype, fieldname):
    menu = Menu.objects.all()

    try:
        pagina_home = PaginaHome.objects.all()[0]
    except:
        pagina_home = PaginaHome()
        pagina_home.save()

    context = dict()
    context['pagina_home'] = pagina_home
    context['menu'] = menu

    if not fieldname or not fieldtype:
        raise Http404("Parametros de edicion requeridos")

    else:
        content = CMSContentManager.get_content_class(fieldtype)
        fieldcontent = get_object_or_404(content, fieldname=fieldname)
        formclass = CMSContentManager.get_content_formclass(fieldtype)

        if not fieldcontent or not formclass:
            raise Http404("No existe modelo para los campos")

        else:
            context['form'] = formclass(instance=fieldcontent)
            context['fieldname'] = fieldname
            context['fieldtype'] = fieldtype

            if request.method == 'GET':
                    return render(request, 'home.html', context=context)

            elif request.method == 'POST':
                    form = formclass(request.POST, request.FILES, instance=fieldcontent)
                    if form.is_valid():
                        form.save()
                        return HttpResponseRedirect(reverse('home'))

                    else:
                        return render(request, 'home.html', context=context)


