#!/usr/bin/env python
# coding: utf-8

# ## 1. Вычисление статистики успеваемости студентов

# In[64]:


students = [
{"name": "Alice", "age": 20, "grades": [85, 90, 88, 92]},
{"name": "Bob", "age": 22, "grades": [78, 89, 76, 85]},
{"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94]},
{"name": "Anna", "age": 21, "grades": [91, 96, 88, 94]}
# ... (другие студенты)
]


# #### а) Фильтрация данных

# Отфильтровать студентов определенного возраста.

# In[65]:


def students_by_age(students, age):
    sort = []
    for student in students:
        if student["age"] == age:
            sort.append(student)
    return sort


# In[106]:


students_by_age(students, 20)


# #### б) Преобразование данных

# Вычислить средний балл для каждого студента и общий средний
# балл по всем студентам.

# In[75]:


def avg_grade(student):
    summ = 0
    for grade in student["grades"]:
        summ += int(grade)
    l = len(student["grades"])
    if l == 0:
        return 0
    return summ/len(student["grades"])

def all_avg_grade(students):
    total = 0
    for student in students:
        total += avg_grade(student)
    l = len(students)
    if l == 0:
        return 0
    return total / len(students)


# In[104]:


print(avg_grade(students[0]))
print(all_avg_grade(students))


# #### в) Агрегация данных

# Найти студента (или студентов) с самым высоким средним баллом.

# In[72]:


def highest_avg_grade(students):
    highest = -1
    top = []
    for student in students:
        avg = avg_grade(student)
        if avg > highest:
            top = []
            highest = avg
            top.append(student)
        elif avg == highest:
            top.append(student)
    return top


# In[105]:


highest_avg_grade(students)


# ## 2. Расчет общей суммы расходов для пользователей с заданными критериями

# In[82]:


users = [
{"name": "Alice", "expenses": [100, 50, 75, 200]},
{"name": "Bob", "expenses": [50, 75, 80, 100]},
{"name": "Charlie", "expenses": [200, 300, 50, 150]},
{"name": "David", "expenses": [100, 200, 300, 400]},
# ... (другие пользователи)
]


# #### а) Отфильтровать пользователей по заданным критериям

# In[101]:


def users_by_crit(users, crit):
    sort = []
    for user in users:
        if all(user.get(key) == value for key, value in crit.items()):
            sort.append(user)
    return sort


# In[102]:


users_by_crit(users, {"name": "Alice"})


# #### б) Для каждого пользователя рассчитать общую сумму его расходов

# In[108]:


def total_exp_user(user):
    return sum(user["expenses"])


# In[109]:


total_exp_user(users[0])


# #### в) Получить общую сумму расходов всех отфильтрованных пользователей

# In[112]:


def total_exp_users(users):
    total = 0
    for user in users:
        total += total_exp_user(user)
    return total


# In[113]:


total_exp_users(users)


# ##  3. Работа с большой базой данных заказов и клиентов

# In[125]:


orders = [
{"order_id": 1, "customer_id": 101, "amount": 150.0},
{"order_id": 2, "customer_id": 102, "amount": 200.0},
{"order_id": 3, "customer_id": 101, "amount": 75.0},
{"order_id": 4, "customer_id": 103, "amount": 100.0},
{"order_id": 5, "customer_id": 101, "amount": 50.0},
# ... (далее по списку)
]


# #### а) Фильтрация заказов

# In[130]:


def orders_by_id(orders, customer_id):
    o = []
    for order in orders:
        if order["customer_id"] == customer_id:
            o.append(order)
    return o


# In[131]:


orders_by_id(orders, 101)


# #### б) Подсчет суммы заказов

# In[132]:


def total_sum(orders):
    return sum(order["amount"] for order in orders)


# In[133]:


total_sum(orders)


# #### в) Подсчет средней стоимости заказов

# In[134]:


def avg_sum(orders):
    l = len(orders)
    if l == 0:
        return 0
    return total_sum(orders) / len(orders)


# In[135]:


avg_sum(orders)

