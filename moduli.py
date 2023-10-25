# первое задание
def all_divisors(num):
    divisors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    divisors.sort()
    return divisors


num = [23436, 190187200, 380457890232]
for num in numbers:
    divisors = all_divisors(num)
    print(f"Делители числа {num}: {divisors}")


# второе задание
def three_args(*, var1=None, var2=None, var3=None):
    args = []
    if var1 is not None:
        args.append(f"var1 = {var1}")
    if var2 is not None:
        args.append(f"var2 = {var2}")
    if var3 is not None:
        args.append(f"var3 = {var3}")

    if args:
        print("Переданы аргументы:", ", ".join(args))
    else:
        print("Аргументы не были переданы.")


three_args(var1=2, var3=10)
three_args(var2="Hello")
three_args(var3=5, var1=None, var2=None)


# третье задание
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))


# четветртое задание
def most_common_and_longest_words(text):
    w = text.lower().split()
    w = [word.strip(".,!?") for word in w]
    word_counts = {}
    for word in w:
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    most_common_word = max(word_counts, key=word_counts.get)
    longest_word = max(w, key=len)
    return most_common_word, longest_word


text = input("Введите текст: ")
most_common, longest = most_common_and_longest_words(text)
print(f"Наиболее часто встречающееся слово: {most_common}")
print(f"Самое длинное слово: {longest}")


# пятое задание
def generate_spiral_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    num = 1
    top, bottom, left, right = 0, n - 1, 0, m - 1

    while num <= n * m:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    return matrix

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
spiral_matrix = generate_spiral_matrix(n, m)

for row in spiral_matrix:
    for num in row:
        print(num, end="\t")
    print()

# шестое задание

def is_magic_square(matrix):
    n = len(matrix)

    expected_sum = sum(matrix[0])

    for i in range(1, n):
        if sum(matrix[i]) != expected_sum:
            return False

    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != expected_sum:
            return False

    if sum(matrix[i][i] for i in range(n)) != expected_sum:
        return False

    if sum(matrix[i][n - i - 1] for i in range(n)) != expected_sum:
        return False

    return True

matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("Это магический квадрат.")
else:
    print("Это не магический квадрат.")