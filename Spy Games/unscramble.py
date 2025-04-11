from collections import defaultdict

def unscrambled():
    def unscramble_from_file(filename, word_list):
        with open(filename, "r") as file:
            scrambled_sentence = file.read().strip().lower()

        sorted_word_map = defaultdict(list)
        for word in word_list:
            key = "".join(sorted(word))
            sorted_word_map[key].append(word)

        unscrambled_words = []
        for scrambled_word in scrambled_sentence.split():
            key = "".join(sorted(scrambled_word))
            matches = sorted_word_map.get(key, [])
            unscrambled_word = matches[0] if matches else scrambled_word
            unscrambled_words.append(unscrambled_word)

        return " ".join(unscrambled_words)


    word_list = [
        "what", "walks", "on", "four", "legs", "in", "the", "morning",
        "two", "at", "noon", "and", "three", "evening"
    ]
    unscrambled = unscramble_from_file("notes.txt", word_list)
    # with open("notes.txt","r") as note:
    #     note1 = note.read()
    return unscrambled
print(unscrambled())