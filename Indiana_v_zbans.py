def generate_password(n):
    pairs = []

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                pairs.append(f"{i}{j}")

    return ''.join(pairs)


n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"{n} - {password}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")