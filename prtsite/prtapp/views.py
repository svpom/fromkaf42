from django.shortcuts import render
from . import trees_root
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.
def main_page(request):
    return render(request, 'prtapp/main_page.html', {})


def summary_about_trees_root(request):
    return render(request, 'prtapp/summary_about_trees_root.html', {})


def cut_method(request):
    return render(request, 'prtapp/cut_method.html', {})


def test_form(request):
    if request.method == "POST":
        tmp = []
        for arg in request:
            tmp.append(arg)
        return render(request, 'prtapp/test_form.html', {"tmp": tmp})
    return render(request, 'prtapp/test_form.html', {})


def get_root(request):
    tmp = request.POST.items()
    # return render(request, 'prtapp/test_form.html', {"tmp": tmp})
    return JsonResponse(tmp)


def xhr_test(request):
    if request.is_ajax():
        if request.method == "POST":
            inp = request.POST.get("inp", "Error. Try again.")
            root_number = trees_root.clip_met(inp[:-1])  # -1 is to delete last ;

    return HttpResponse(root_number)
