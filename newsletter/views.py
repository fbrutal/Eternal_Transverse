from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.

def home(request):
    if request.method == 'POST': # пару проверок формы
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() # сохраняем нашу форму в базу
            all_is_right = "Ваше сообщение успешно отправлено."
            form = SignUpForm()
            # очищаем форму

    else:
        form = SignUpForm()
    return render(request,'home.html', {
        'form': form,
        # 'all_is_right': all_is_right,
        })
