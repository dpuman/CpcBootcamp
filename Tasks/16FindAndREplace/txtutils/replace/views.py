from django.shortcuts import render
import os

# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'replace/index.html')

    if request.method == 'POST':

        filein = request.POST.get('filein')
        ftext = request.POST.get('ftext')
        replace = request.POST.get('replace')

        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, filein)

        file = open(file_path, 'r')
        f = file.read()
        file.close()

        nfile = f.replace(ftext, replace)

        filehandler = open('replaced.txt', 'w')
        filehandler.write(nfile)
        filehandler.close()

        contex = {
            'filein': nfile
        }

        return render(request, 'replace/index.html', contex)
