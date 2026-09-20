from django.shortcuts import render


def index(request):

    data = {
        'title': 'Главная страница',
        'description': 'Добро пожаловать на мой сайт!',
        'items': [
            'Первый элемент',
            'Второй элемент',
            'Третий элемент'
        ]
    }

    return render(request, 'index.html', data)


def about(request):

    data = {
        'title': 'О нас',
        'description': 'Информация о нашем сайте.',
        'items': [
            'История сайта',
            'Наша команда',
            'Наши цели'
        ]
    }

    return render(request, 'about.html', data)


def services(request):

    data = {
        'title': 'Услуги',
        'description': 'Наши основные услуги.',
        'items': [
            'Разработка сайтов',
            'Создание дизайна',
            'Техническая поддержка'
        ]
    }

    return render(request, 'services.html', data)


def contacts(request):

    data = {
        'title': 'Контакты',
        'description': 'Свяжитесь с нами.',
        'items': [
            'Телефон: +7 (900) 000-00-00',
            'Email: example@mail.ru',
            'Адрес: Россия'
        ]
    }

    return render(request, 'contacts.html', data)


def gallery(request):

    data = {
        'title': 'Галерея',
        'description': 'Галерея нашего сайта.',
        'items': [
            'Изображение №1',
            'Изображение №2',
            'Изображение №3'
        ]
    }

    return render(request, 'gallery.html', data)

# Create your views here.
