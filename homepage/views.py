from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <body style="background-color: #b424d1; min-height: 100vh; padding: 20px; font-family: 'Segoe UI';">
            <h1>Miguel</h1>
            <p>Miguel</p> 
            <p>Miguel</p>
        </body>
    """
            #Ini adalah baris baru menggunakan teks biasa.
            #Sekarang latar belakang halaman sudah berubah warna!

                        #"<h1>Portfolio Saya</h1>"
        #"<p>Ini adalah baris baru menggunakan teks biasa.</p>"
        #"<p>Ini baris baru berikutnya. Anda juga bisa memotong baris<br>"
        #"tepat di tengah kalimat seperti ini menggunakan tag br.</p>"
        )
