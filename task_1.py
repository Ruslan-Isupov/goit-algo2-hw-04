from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")

        return sum(1 for word in self.keys() if word.endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")

        return self.has_node(prefix)


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    print(
        f"Count of words ending with 'e': {trie.count_words_with_suffix('e')} (Expected: 1)"
    )
    assert trie.count_words_with_suffix("e") == 1  # apple
    print(
        f"Count of words ending with 'ion': {trie.count_words_with_suffix('ion')} (Expected: 1)"
    )
    assert trie.count_words_with_suffix("ion") == 1  # application
    print(
        f"Count of words ending with 'a': {trie.count_words_with_suffix('a')} (Expected: 1)"
    )
    assert trie.count_words_with_suffix("a") == 1  # banana
    print(
        f"Count of words ending with 'at': {trie.count_words_with_suffix('at')} (Expected: 1)"
    )
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    print(f"Does 'app' exist as a prefix? {trie.has_prefix('app')} (Expected: True)")
    assert trie.has_prefix("app") == True  # apple, application
    print(f"Does 'bat' exist as a prefix? {trie.has_prefix('bat')} (Expected: False)")
    assert trie.has_prefix("bat") == False
    print(f"Does 'ban' exist as a prefix? {trie.has_prefix('ban')} (Expected: True)")
    assert trie.has_prefix("ban") == True  # banana
    print(f"Does 'ca' exist as a prefix? {trie.has_prefix('ca')} (Expected: True)")
    assert trie.has_prefix("ca") == True  # cat
