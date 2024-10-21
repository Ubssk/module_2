def generate_password(number):
    if not (3 <= number <= 20):
        return
    password = ""
    pairs = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if i != number and j != number:
                pairs.append((i, j))
    for (a, b) in pairs:
        pair_sum = a + b
        if number % pair_sum == 0:
            password += f"{a}{b}"
    return password

# Все пароли для чисел от 3 до 20
for i in range(3, 21):
    generated_password = generate_password(i)
    print(f"{i} - {generated_password}")

while True:
    try:
        first_number = int(input('Введите число на камне в первом поле (от 3 до 20): '))

        if first_number < 3 or first_number > 20:
            print("Число должно быть в диапазоне от 3 до 20.")

        else:
            generated_password = generate_password(first_number)
            print(f"Пароль для {first_number} - {generated_password}")
            break

    except ValueError:
        print("Пожалуйста, введите корректное целое число.")