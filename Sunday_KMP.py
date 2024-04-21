import random


def matches_at(text, pattern, position, comparisons):
    for i in range(len(pattern)):
        comparisons += 1
        if text[position + i] != pattern[i]:
            return False, comparisons
    return True, comparisons


def naive(text, pattern):
    comparisons = 0
    text_length = len(text)
    pattern_length = len(pattern)
    occurrences = []
    for p in range(text_length - pattern_length + 1):
        matched, comparisons = matches_at(text, pattern, p, comparisons)
        if matched:
            occurrences.append(p)
    return occurrences, comparisons


def wystapienia(pattern):
    indeksy = {}
    dlugosc = len(pattern)
    for indeks, litera in enumerate(pattern):
        indeksy[litera] = dlugosc - indeks
    indeksy['W'] = dlugosc + 1
    return indeksy


def sunday(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0
    occurrences = []
    shifts = wystapienia(pattern)
    i = 0
    while i <= n - m:
        matched, comparisons = matches_at(text, pattern, i, comparisons)
        if matched:
            occurrences.append(i)
        if i + m < n:
            next_char = text[i + m]
            if next_char in shifts:
                i += shifts[next_char]
            else:
                i += shifts['W']
        else:
            break
    return occurrences, comparisons


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0
    kmp_next = [-1]
    b = -1
    for i in range(1, m + 1):
        while b > -1 and pattern[b] != pattern[i - 1]:
            comparisons += 1
            b = kmp_next[b]
        b += 1
        if i == m or pattern[i] != pattern[b]:
            kmp_next.append(b)
        else:
            kmp_next.append(kmp_next[b])
    occurrences = []
    b = 0
    for i in range(n):
        while b > -1 and pattern[b] != text[i]:
            comparisons += 1
            b = kmp_next[b]
        b += 1
        if b == m:
            occurrences.append(i - m + 1)
            b = kmp_next[b]
    return occurrences, comparisons


# Generowanie losowego tekstu i wzorca
def generate_random_text(length, alphabet):
    return ''.join(random.choice(alphabet) for _ in range(length))


def generate_random_pattern(length, alphabet):
    return ''.join(random.choice(alphabet) for _ in range(length))


def test_algorithms_with_random_text():
    text_length = 50
    pattern_length = 5
    alphabet_size = 4

    alphabet = [chr(ord('A') + i) for i in range(alphabet_size)]
    text = generate_random_text(text_length, alphabet)
    pattern = generate_random_pattern(pattern_length, alphabet)

    print("Generated Text:", text)
    print("Generated Pattern:", pattern)
    print()

    algorithms = [naive, sunday, kmp_search]
    for algorithm in algorithms:
        occurrences, comparisons = algorithm(text, pattern)
        print(f"Algorithm: {algorithm.__name__}")
        print("Occurrences found at positions:", occurrences)
        print("Number of comparisons:", comparisons)
        print("\n")


test_algorithms_with_random_text()
