import random
numbers = [random.randint(0, 100) for i in range(20)]
print(numbers)
a = random.randint(0, 100)
print(f"Число {a} есть в списке" if a in numbers else f"Числа {a} нет в списке")


marks = ["Audi", "Lada", "Toyota", "Bentley", "Haval"]
x = random.choice(marks)
print(f"Марка {x} не под санкциями" if x in ["Lada", "Haval"] else f"Марка {x} под санкциями")


prost = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
n = random.randint(1, 100)
print(f"Число {n} простое" if n in prost else f"Число {n} не является простым")
