from django.shortcuts import render, redirect
from django.http import HttpResponse


quick_fix_auth=[
    '39418a5e8c991009eb3c52c807ae1848',
'07b887178cb2ae2a73e8a0cb0dbc1b5a',
'bf125964385d10245e069301862c99ba',
'607d2c07f80fceeb4a4202143fa5d045',
'267b5c53ccdbc99d5248b163491936b5',
'85d51bf457e8626f6583e112b8161db4',
'a05d842db765f8fadf2b979285c73bfd',
'9854ef18d2b60d4db0af189662a9638b',
'6b01944b47c4bb6521547a96b3365510',
'47628eac5c1a77497d2b7e3723d4ec0d'
]


# Create your views here.

def dashboard(request):
    auth = request.session.get('auth', '')
    # print(auth)
    if(auth in quick_fix_auth):
        # request.session['auth'] = ''
        return render(request, 'index.html', {'total':150,'active':140, 'critical':10 })
    else:
        return redirect('/login')
def mainpage(request):
    return HttpResponse('Hello')