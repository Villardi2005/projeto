from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def login(request):
     return render(request, 'login.html')

def cadastro(request):
     return render(request, 'cadastro.html')

def cadastro_aluno(request):
     return render(request, 'cadastro.html')

def metas(request):
    return render(request, 'metas.html')

def saldoacumulado(request):
    return render(request, 'saldoacumulado.html')

def chat(request):
    return render(request, 'chat.html')

def recompensas(request):
    return render(request, 'recompensas.html')

def professor(request):
    return render(request, 'professor.html')

def responsavel(request):
    return render(request, 'responsavel.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if senha == 'teste':
            if email == 'alunoteste@gmail.com':
                return render(request, 'metas.html')
            elif email == 'profteste@gmail.com':
                return render(request, 'professor.html')
            elif email == 'respteste@gmail.com':
                return render(request, 'responsavel.html')

        erro = "E-mail ou senha incorretos"
        return render(request, 'login.html', {'erro': erro})

    return render(request, 'login.html')
