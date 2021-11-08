from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# class Position(models.Model):
#     name = models.CharField(max_length=255)
#     department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)     # �.�. � ���� ������� ��� ������ ����, ������� ���������� ���� �������� defaut ���� �������� Null
#
#     def __str__(self):
#         return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    is_married = models.BooleanField(default=False)
    department = models.Model(Department, on_delete=models.PROTECT, null=True)
    # position = models.ForeignKey(Position, on_delete=models.PROTECT, null=True)
    # department = models.ForeignKey(Position.dep_pos, on_delete=models.PROTECT, null=True)  # �.�. � ���� ������� ��� ������ ����, ������� ���������� ���� �������� defaut ���� �������� Null




