def number_to_words(num):
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    thousands = ["", "тысяча", "тысячи", "тысяч"]

    if num == 0:
        return "ноль"
    elif num < 0:
        return "минус " + number_to_words(abs(num))

    words = ""

    if num // 1000 > 0:
        if num // 1000 == 1:
            words += thousands[1] + " "
        elif num // 1000 in [2, 3, 4]:
            words += ones[num // 1000] + " " + thousands[2] + " "
        else:
            words += ones[num // 1000] + " " + thousands[3] + " "
        num %= 1000

    if num // 100 > 0:
        words += hundreds[num // 100] + " "
        num %= 100

    if num >= 10 and num <= 19:
        words += tens[num - 10] + " "
    else:
        if num // 10 > 0:
            words += tens[num // 10] + " "
            num %= 10

        if num > 0:
            words += ones[num] + " "

    return words.strip()

# Тестирование функции
num = int(input("Введите число: "))
words = number_to_words(num)
print(words)