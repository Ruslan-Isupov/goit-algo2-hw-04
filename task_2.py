from trie import Trie


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""

        prefix = strings[0]
        for word in strings[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


if __name__ == "__main__":
    trie = LongestCommonWord()

    strings = ["flower", "flow", "flight"]
    result = trie.find_longest_common_word(strings)
    print(f"Longest common prefix of {strings}: {result} (Expected: 'fl')")
    assert result == "fl"

    strings = ["interspecies", "interstellar", "interstate"]
    result = trie.find_longest_common_word(strings)
    print(f"Longest common prefix of {strings}: {result} (Expected: 'inters')")
    assert result == "inters"

    strings = ["dog", "racecar", "car"]
    result = trie.find_longest_common_word(strings)
    print(f"Longest common prefix of {strings}: {result} (Expected: '')")
    assert result == ""
