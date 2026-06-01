import string


def word_frequency_analyzer(text):
    text = text.lower()

    for mark in string.punctuation:
        text = text.replace(mark, "")

    words = text.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    sorted_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return word_dict, sorted_words[:5]


print("=== Word Frequency Analyzer ===")
print("Please enter  your paragraph below (and press Enter):\n")

user_text = input()

total_words_dict, top_5_words = word_frequency_analyzer(user_text)

print("\n--- Report ---")
print(f"Total unique words in the text: {len(total_words_dict)}")

print("\nTop 5 most used words:")
for word, count in top_5_words:
    print(f" -> '{word}': {count} times")
