from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator


from core.erp.forms import PacienteForm
from core.erp.models import Paciente, Administrador


def lista_paciente(request):
    data = {
        'title': 'Listado de pacientes',
        'pacientes': Paciente.objects.all()
    }
    return render(request, 'paciente/lista.html', data)


class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente/lista.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)   

    def post(self, request, *args, **kwargs):
        data = {}

        try:
            data = Paciente.objects.get(pk=request.POST['id']).toJSON
        except Exception as e:
            data['error'] = str(e)
        
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de pacientes'
        context['url_crear'] = reverse_lazy('erp:paciente_crear')
        context['url_listar'] = reverse_lazy('erp:paciente_listar')
        context['paciente_slidebar'] = reverse_lazy('erp:paciente_listar')
        #context['object_list'] = Administrador.objects.all()
        return context


class PacienteCrearView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/crearP.html'
    success_url = reverse_lazy('erp:paciente_listar')


    #--- AJAX -----
    # def post(self, request, *args, **kwargs):
    #     data = {}

    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             if form.is_valid():
    #                 form.save()
    #             else:
    #                 data['error'] = form.errors
    #         else:
    #             data['error'] = 'No ha ingresado ninguna opcioón'
    #         data = Paciente.objects.get(pk=request.POST['id']).toJSON
    #     except Exception as e:
    #         data['error'] = str(e)
        
    #     return JsonResponse(data)
    #--- AJAX -----

    # def post (self, request, *args, **kwargs):
    #     form = PacienteForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar paciente'
        context['cancelarcrearpaciente'] = reverse_lazy('erp:paciente_listar')
        context['paciente_slidebar'] = reverse_lazy('erp:paciente_listar')
        context['action'] = 'add'
        
        #context['object_list'] = Administrador.objects.all()
        return context


class PacienteUpdateView(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente/crearP.html'
    success_url = reverse_lazy('erp:paciente_listar')

    # def dispatch(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     return super().dispatch(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     data = {}

    #     try:
    #         data = Paciente.objects.get(pk=request.POST['id']).toJSON
    #     except Exception as e:
    #         data['error'] = str(e)
        
    #     return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar paciente'
        context['cancelarcrearpaciente'] = reverse_lazy('erp:paciente_listar')
        context['paciente_slidebar'] = reverse_lazy('erp:paciente_listar')
        context['action'] = 'add'
        
        #context['object_list'] = Administrador.objects.all()
        return context

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente/borrarP.html'
    success_url = reverse_lazy('erp:paciente_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar paciente'    
        context['paciente_slidebar'] = reverse_lazy('erp:paciente_listar')
        context['cancelarcrearpaciente'] = reverse_lazy('erp:paciente_listar')

        return context