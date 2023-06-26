from django.shortcuts import render
from trabalho1app.models import Aluno
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    aluno = Aluno.objects.all()
    testChave = {
        'curso': 'Desenvolvimento Web',
        'alunos': aluno
    }
    return render(request,'index.html', testChave)



def aluno(request, id):

    aluno = Aluno.objects.get(id=id)
    context = {

    'aluno': aluno

    }
    return render(request, 'aluno.html', context)


@csrf_exempt
def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')


        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"Mensagem: {mensagem}")

        return render(request, 'contato.html')

    return render(request, 'contato.html')