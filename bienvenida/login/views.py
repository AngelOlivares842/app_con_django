from django.shortcuts import render, get_object_or_404, redirect
from .models import User

# Create your views here.
def User(request, pk):
    users = get_object_or_404(User, pk=pk)
    return render(request, 'inventario/producto_detail.html',
    {'object': users})