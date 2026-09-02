from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Halo! Ini adalah halaman utama Portfolio saya yang baru diubah.</h1>")
