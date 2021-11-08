from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
from django.views import generic



class EmployeeListView(generic.ListView):
    model = Employee
    template_name = "index.html"
    from_class = EmployeeForm


class EmployeeCreateView(generic.CreateView):
    model = Employee
    fields = ["full_name", "username", "address", "email", "phone_number", "salary", "is_married"]
    template_name = "index.html"
    success_url = "/employees/list/"


def index(request):

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if not form.is_valid():
            return render(request, template_name="errors.html", context={"error": form.errors})

        is_married_mapper = {
            "on": True,
            "off": False
        }
        # print(form.data["is_married"])

        Employee.objects.create(
            full_name=form.data["full_name"],
            username=form.data["username"],
            address=form.data["address"],
            email=form.data["email"],
            phone_number=form.data["phone_number"],
            salary=form.data["salary"],
            is_married=is_married_mapper.get(form.data["is_married"], False)
        )
        # print(form.data)
    form = EmployeeForm()
    employees = Employee.objects.all()
    return render(request, template_name="index.html", context={"form": form, "employees": employees})
