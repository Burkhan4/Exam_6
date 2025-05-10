from django.shortcuts import render, get_object_or_404, redirect
from .models import Poet
from .forms import PoetForm
from django.contrib.auth.decorators import login_required

def poet_list(request):
    poets = Poet.objects.all()
    return render(request, 'uzbek_poets/poet_list.html', {'poets': poets})

@login_required
def poet_create(request):
    if request.method == 'POST':
        form = PoetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poet_list')
    else:
        form = PoetForm()
    return render(request, 'uzbek_poets/poet_form.html', {'form': form})

@login_required
def poet_edit(request, pk):
    poet = get_object_or_404(Poet, pk=pk)
    if request.method == 'POST':
        form = PoetForm(request.POST, instance=poet)
        if form.is_valid():
            form.save()
            return redirect('poet_list')
    else:
        form = PoetForm(instance=poet)
    return render(request, 'uzbek_poets/poet_form.html', {'form': form})

@login_required
def poet_delete(request, pk):
    poet = get_object_or_404(Poet, pk=pk)
    poet.delete()
    return redirect('poet_list')
