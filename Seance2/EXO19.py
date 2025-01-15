word_counts = {}
total_words = 0

while True:
    word = input("Enter a word: ").strip()
    total_words += 1

    if word in word_counts:
        print(f"\nYou typed {total_words} words in total.")
        print(f"You typed in {len(word_counts)} unique words.")
        print("Unique words (alphabetically):", sorted(word_counts.keys()))

        
        print("\nOccurrences of words:")
        for w, count in word_counts.items():
            print(f"{w}: {count} times")
        break

    
    word_counts[word] = word_counts.get(word, 0) + 1

