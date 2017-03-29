from django.shortcuts import render
from . import trees_root
from django.http import HttpResponse
from .forms import UploadImageToEncodeForm, UploadImageToDecodeForm
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
    form_to_encode = UploadImageToEncodeForm()
    form_to_decode = UploadImageToDecodeForm()
    return render(request, 'prtapp/stegano_in_images.html',
                  {'form_to_encode': form_to_encode, 'form_to_decode': form_to_decode})


def upload_image_to_encode(request):
    if request.method == "POST":
        form_to_encode = UploadImageToEncodeForm(request.POST, request.FILES)
        form_to_decode = UploadImageToDecodeForm()  # for errors
        if form_to_encode.is_valid():
            f = request.FILES['img']
            if f.size < 20000000:  # <20MB
                mes = request.POST['mes']
                err = encode_image(mes, f)  # mes is user's message

                if err != "":
                    return render(request, 'prtapp/stegano_in_images.html',
                                  {'form_to_encode': form_to_encode, 'err': err, 'form_to_decode': form_to_decode})
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
                os.remove('prtapp/media/images/input/' + f.name)
                os.remove(path_to_result)
                return response

        form_to_encode = UploadImageToEncodeForm()
    return render(request, 'prtapp/stegano_in_images.html',
                  {'form_to_encode': form_to_encode, 'form_to_decode': form_to_decode})


def encode_image(mes, f):
    path_to_encoded_image = 'prtapp/media/images/input/' + f.name
    err = ""

    dest = open(path_to_encoded_image, 'wb+')  # save img to disk from UploadedFile 
    for chunk in f.chunks():
        dest.write(chunk)
    dest.close()

    img = Image.open(path_to_encoded_image)
    if int(img.height * img.width / 10) < len(mes):  # 10=1+2+3+4 pixels - from generator
        img.close()
        err = "Слишком длинное сообщение. Уменьшите длину сообщения или выберите файл большего размера."
        return err

    steg_img.encode_mes(mes, img, f.name)
    img.close()
    return err


def upload_image_to_decode(request):
    if request.method == "POST":
        form_to_decode = UploadImageToDecodeForm(request.POST, request.FILES)
        if form_to_decode.is_valid():
            f = request.FILES['img']
            if f.size < 20000000:  # <20MB
                mes_len = request.POST['mes_len']
                dec_mes = decode_image(mes_len, f)  # dec - decoded
                os.remove('prtapp/media/images/input/' + f.name)

                return HttpResponse("Закодированное сообщение: " + dec_mes)

        form_to_encode = UploadImageToEncodeForm()
    return render(request, 'prtapp/stegano_in_images.html',
                  {'form_to_encode': form_to_encode, 'form_to_decode': form_to_decode})


def decode_image(mes_len, f):
    path_to_encoded_image = 'prtapp/media/images/input/' + f.name

    dest = open(path_to_encoded_image, 'wb+')  # save img to disk from UploadedFile 
    for chunk in f.chunks():
        dest.write(chunk)
    dest.close()

    img = Image.open(path_to_encoded_image)

    dec_mes = steg_img.decode_mes(img, mes_len)
    return dec_mes


def stegano_in_videos(request):
    return render(request, 'prtapp/stegano_in_videos.html', {})


def contacts(request):
    return render(request, 'prtapp/contacts.html', {})
