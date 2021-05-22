from django.shortcuts import render

# Create your views here.


def index(request):
    string = request.GET.get('text')

    try:
        string_split = string.split()

        string_dict = {}
        string_length = len(string_split)

        for str in string_split:
            if str in string_dict:
                string_dict[str] += 1
            else:
                string_dict[str] = 1
        context = {
            'string_length': string_length,
            'string_dict': string_dict

        }

        return render(request, 'counter/index.html', context)
    except:
        return render(request, 'counter/index.html')
