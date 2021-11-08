"""
class EmployeeForm(forms.Form):    #валидация
    pass

    form = EmployeeForm(request.POST) - создали объект класса

    request - объект запроса
    request.POST - вызываем атрибрут класса(объекта)
    is_valid - возвращает валидацию, проверять форму параметра на ошибки
        (валидно ли) - возвращает True и False: если вернул True,
        то без ошибок
template_name - имя шаблона
CRUD - create, read, update, delete
    МЕТОДЫ ЗАПРОСА:
        POST - create(создание(отправлять) данных)
        GET - listing, retrieve(весь список достать)
        PUT(все), PATCH(определенное поле) - update(обновлять)
        DELETE - deletion(удалять)

{% csrf_token %} - вид защиты от внешнего доступа - только для html
2 types of web apps:
    SER - server side rendering
    SPA - single page application

MVC - Model, View, Controller(urls)
generic - шаблонизатор(без него не возможно передавать данные)
form.data - отвалидованные данные
employees = Employee.objects.all() - запрашивают все данные с таблицы
"""
