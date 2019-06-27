# 2. Вывод на одной строке
header = [
        'Название', 'EmojiXpress, млн', 'Instagram, млн', 'Твиттер, млн'
]

# < напишите код здесь >
print('', end='| ')
for count in header:
    print(count, end=' | ')