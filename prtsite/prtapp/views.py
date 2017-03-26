from django.shortcuts import render
from . import trees_root
from django.http import HttpResponse


# Create your views here.
def main_page(request):
    return render(request, 'prtapp/main_page.html', {})


def summary_about_trees_root(request):
    return render(request, 'prtapp/summary_about_trees_root.html', {})


def cut_method(request):
    return render(request, 'prtapp/cut_method.html', {})


def xhr_cut(request):
    if request.is_ajax():
        if request.method == "POST":
            inp = request.POST.get("inp", "Error. Try again.")
            root_number = trees_root.clip_met(inp[:-1])  # -1 is to delete last ;
    return HttpResponse(root_number)


def based_on_tops_height(request):
    return render(request, 'prtapp/based_on_tops_height.html', {})


def xhr_height(request):
    if request.is_ajax():
        if request.method == "POST":
            inp = request.POST.get("inp", "Error. Try again.")
            root_number = trees_root.height_met(inp[:-1])  # -1 is to delete last ;
    return HttpResponse(root_number)

def summary_about_stegano(request):
    return render(request, 'prtapp/summary_about_stegano.html', {})