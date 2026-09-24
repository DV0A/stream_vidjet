from django.shortcuts import render


def widgets(request):
    return render(request, 'widgets/widget.html')
