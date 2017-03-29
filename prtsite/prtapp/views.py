from django.shortcuts import render
from . import trees_root
from django.http import HttpResponse
from .forms import UploadImageForm
from . import steg_img
from PIL import Image
import os
import mimetypes

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


def stegano_in_images(request):
    form = UploadImageForm()
    return render(request, 'prtapp/stegano_in_images.html', {'form': form})


def upload_image(request):
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['img']
            if f.size < 20000000:  # <100MB
                mes = "12234566"
                encode_image(mes, f)  # mes is user's message
                path_to_result = 'prtapp/media/images/output/' + f.name
                fp = open(path_to_result, "rb")
                response = HttpResponse(fp.read())
                fp.close()
                file_type = mimetypes.guess_type(path_to_result)
                if file_type is None:
                    file_type = 'application/octet-stream'
                response['Content-Type'] = file_type
                response['Content-Length'] = str(os.stat(path_to_result).st_size)
                response['Content-Disposition'] = "attachment; filename='%s'" % f.name
                return response
               # return render(request, 'prtapp/download_result.html', {'url': url})
    else:
        form = UploadImageForm()
    return render(request, 'prtapp/stegano_in_images.html', {'form': form})


def encode_image(mes, f):
    path_to_encoded_image = 'prtapp/media/images/input/' + f.name
    dest = open(path_to_encoded_image, 'wb+')  # save img to disk from UploadedFile 
    for chunk in f.chunks():
        dest.write(chunk)
    dest.close()

    steg_img.encode_mes(mes, Image.open(path_to_encoded_image), f.name)
