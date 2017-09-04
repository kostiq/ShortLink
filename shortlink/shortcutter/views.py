from django import forms
from django.shortcuts import render, redirect


class MainForm(forms.Form):
    link = forms.CharField(max_length=500)


def index(request):
	print(request, request.GET, request.POST)
	form = MainForm()
	return render(request, 'index.html', context={'form': form})


def redirect_full_link(request, link_id):
    # link = Links.objects.get(id=link_id)
    return redirect('http://stackoverflow.com/')


def shortcut(request):
    pass
