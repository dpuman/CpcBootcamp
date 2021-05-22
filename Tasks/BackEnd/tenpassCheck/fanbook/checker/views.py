from django.shortcuts import render
import re

# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request,'checker/index.html')
    if request.method=='POST':
        password=request.POST['u-password']

        message = ''
        invalid=''
        x = True
        while x:
            if len(password) < 8:
                message = 'At least 8 digit'
                break
            elif re.findall("^1|0|2|3|4|5|6|7|8|9", password):
                message = "First digit can't be number"
                break
            elif not re.search('[A-Z]', password):
                message = 'At least one Uppercase'
                break
            elif not re.search('[a-z]', password):
                message = 'At least one lowercase'
                break
            elif not re.search('[@#$_]', password):
                message = 'Must contain at least one special character'
                break

            else:
                message = 'Success with a Valid password'
                x = False
                break
        if x:
            invalid='Password is not valid'

        context={
            'message':message,
            'invalid':invalid

        }

        return render(request,'checker/message.html',context)