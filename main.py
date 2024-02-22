from functools import reduce


# 1. Вычисление статистики успеваемости студентов

students = [
{"name": "Alice", "age": 20, "grades": [85, 90, 88, 92]},
{"name": "Bob", "age": 22, "grades": [78, 89, 76, 85]},
{"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94]},
{"name": "Anna", "age": 21, "grades": [91, 96, 88, 94]}
# ... (другие студенты)
]


# а) Фильтрация данных

def students_by_age(students, age):
    return list(filter(lambda student: student['age'] == age, students))
print(students_by_age(students, 20))


# б) Преобразование данных
# Вычислить средний балл для каждого студента и общий средний
# балл по всем студентам.

def avg_grade(student):
    return sum(student["grades"]) / len(student["grades"])

def all_avg_grade(students):
    total_num_grades = sum(map(lambda student: len(student['grades']), students))
    total_grades_sum = reduce(lambda acc, student: acc + sum(student['grades']), students, 0)
    return total_grades_sum / total_num_grades

print(avg_grade(students[0]))
print(all_avg_grade(students))


# в) Агрегация данных
# Найти студента (или студентов) с самым высоким средним баллом.

def highest_avg_grade(students):
    highest_avg = max(map(lambda student: avg_grade(student), students))
    highest_avg_students = filter(lambda student: avg_grade(student) == highest_avg, students)
    return list(highest_avg_students)
    
print(highest_avg_grade(students))


# 2. Расчет общей суммы расходов для пользователей с заданными критериями

users = [
{"name": "Alice", "expenses": [100, 50, 75, 200]},
{"name": "Bob", "expenses": [50, 75, 80, 100]},
{"name": "Charlie", "expenses": [200, 300, 50, 150]},
{"name": "David", "expenses": [100, 200, 300, 400]},
# ... (другие пользователи)
]


# а) Отфильтровать пользователей по заданным критериям

def filter_users(users, criteria):
    return list(filter(criteria, users))
    
filtered_users = filter_users(users, lambda user: sum(user['expenses']) > 300)
print(filtered_users)

# б) Для каждого пользователя рассчитать общую сумму его расходов

def total_exp_user(user):
    return {"name": user["name"], "total_expenses": sum(user["expenses"])}
    
users_total_expenses = list(map(total_exp_user, users))
print(users_total_expenses)


# в) Получить общую сумму расходов всех отфильтрованных пользователей

def total_exp_users(filtered_users):
    return reduce(lambda acc, user: acc + sum(user['expenses']), filtered_users, 0)

print(total_exp_users(users))


# 3. Работа с большой базой данных заказов и клиентов

orders = [
{"order_id": 1, "customer_id": 101, "amount": 150.0},
{"order_id": 2, "customer_id": 102, "amount": 200.0},
{"order_id": 3, "customer_id": 101, "amount": 75.0},
{"order_id": 4, "customer_id": 103, "amount": 100.0},
{"order_id": 5, "customer_id": 101, "amount": 50.0},
# ... (далее по списку)
]


# а) Фильтрация заказов

def orders_by_id(orders, customer_id):
    return list(filter(lambda order: order['customer_id'] == customer_id, orders))

print(orders_by_id(orders, 101))


# б) Подсчет суммы заказов

def total_sum(orders):
    return reduce(lambda acc, order: acc + order['amount'], orders, 0)
    
print(total_sum(orders))


# в) Подсчет средней стоимости заказов

def avg_sum(orders):
    return total_sum(orders) / len(orders)

print(avg_sum(orders))

