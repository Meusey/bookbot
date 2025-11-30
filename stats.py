
def get_word_count(text):
    words = text.split()
    return len(words)

def count_letters(text):
    counts = {}

    for char in text:
        if char.isalpha():
            char = char.lower()
            counts[char] = counts.get(char, 0) + 1

    return counts

def sort_char(text):
    counts = count_letters(text)
    sorted_counts = sorted(
        [{"char": k, "num": v} for k, v in counts.items()],
        key=lambda x: x["num"],
        reverse=True
    )
    return sorted_counts