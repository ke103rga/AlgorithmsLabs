def generate_skip_table(pattern):
    pat_len = len(pattern)
    skip_table = {ch: max(1, pat_len - ind - 1) for ind, ch in enumerate(pattern)}
    return skip_table


def print_text_with_idx(text):
    [print(str(ind).ljust(3), end=" ") for ind in range(len(text))]
    print()
    [print(str(ch).ljust(3), end=" ") for ch in text]
    print()


def boyer_moore_search(text, pattern):

    skip_table = generate_skip_table(pattern)
    pat_len = len(pattern)
    cur_idx = pat_len - 1
    answer = []
    while cur_idx <= len(text) - 1:
        found = True
        for i in range(pat_len-1, -1, -1):
            if pattern[i] != text[cur_idx - pat_len + i + 1]:
                shift = skip_table.get(text[cur_idx - pat_len + i + 1], pat_len)
                cur_idx += shift
                found = False
                break
        if found:
            answer.append(cur_idx - pat_len + 1)
            cur_idx += pat_len
    return answer


def test():
    print("Firstly, let's demonstrate that method can find single elements")
    single_elem_text = "abcdafdera"
    print("Text for searching:")
    print_text_with_idx(single_elem_text)
    print(boyer_moore_search(single_elem_text, "a"))
    print("We searched char 'a' and as you can see, method can find it in all possible places in text", end="\n\n")

    print("After it let's try to find words")
    words_text = "text which starts with word text and contains some other words except text"
    print("Text for searching:")
    print_text_with_idx(words_text)
    print(boyer_moore_search(words_text, "text"))
    print("We searched word 'text' and as you can see, method can find it in all possible places in text", end="\n\n")

    print("And finally, let's check some specific cases, first of them is situation "
          "when text and pattern are the same")
    same_text = "pattern"
    print("Text for searching:")
    print_text_with_idx(same_text)
    print(boyer_moore_search(same_text, "pattern"))
    print("We searched word 'pattern' and we became convinced that method can deal with it.", end="\n\n")

    print("And the second one is situation when the whole text is repeated pattern")
    repeated_text = "aaaaaaaaaaaaaa"
    print("Text for searching:")
    print_text_with_idx(repeated_text)
    print(boyer_moore_search(repeated_text, "a"))
    print("We searched word 'a' and we became convinced that method can deal with it.", end="\n\n")


test()
