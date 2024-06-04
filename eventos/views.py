from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Evento
from .forms import EventoForm


def pagina_inicial(request):
    eventos_futuros = Evento.objects.filter(data__gte=timezone.now()).order_by('data')
    return render(request, 'eventos/pagina_inicial.html', {'eventos': eventos_futuros})

def detalhe_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'eventos/detalhe_evento.html', {'evento': evento})

@login_required
def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.criador = request.user
            evento.save()
            return redirect('pagina_inicial')
    else:
        form = EventoForm()
    return render(request, 'eventos/criar_evento.html', {'form': form})

@login_required
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.user == evento.criador:
        if request.method == 'POST':
            form = EventoForm(request.POST, instance=evento)
            if form.is_valid():
                form.save()
                return redirect('detalhe_evento', evento_id=evento.id)
        else:
            form = EventoForm(instance=evento)
        return render(request, 'eventos/editar_evento.html', {'form': form})
    else:
        return redirect('pagina_inicial')  # Redirecionar para a página inicial se o usuário não for o criador do evento

@login_required
def excluir_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.user == evento.criador:
        evento.delete()
    return redirect('pagina_inicial')
