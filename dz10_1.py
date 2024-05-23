import pulp

# Створення проблеми максимізації
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості вироблених напоїв
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Обмеження на ресурси
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
problem += 1 * lemonade <= 50, "Sugar_Constraint"
problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Функція цілі: максимізація загальної кількості вироблених напоїв
problem += lemonade + fruit_juice, "Total_Production"

# Розв'язання задачі
problem.solve()

# Виведення результатів
print(f"Статус розв'язку: {pulp.LpStatus[problem.status]}")
print(f"Кількість виробленого Лимонаду: {lemonade.varValue}")
print(f"Кількість виробленого Фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість вироблених напоїв: {pulp.value(problem.objective)}")
