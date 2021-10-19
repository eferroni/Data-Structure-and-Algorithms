words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 15


def text_justification(words, maxWidth):
    length = 0
    line = []
    text = []
    for word in words:
        if length + len(word) > maxWidth:
            length = 0
            text.append(line)
            line = []
        length += len(word) + 1
        line.append(word)
    text.append(line)

    for i in range(len(text)):
        total_length = len("".join(text[i]))

        # one word - left justify
        if len(text[i]) == 1:
            if total_length < maxWidth:
                text[i].append(" " * (maxWidth - total_length))

        # last line - left justify
        elif i == len(text) - 1:
            count = 0
            for x in range(len(text[i]) - 1):
                count += 1
                text[i].insert(x + 1 * count, " ")
            total_length = len("".join(text[i]))
            if total_length < maxWidth:
                text[i].append(" " * (maxWidth - total_length))
        else:
            # N word - justify
            empty_n = (maxWidth - total_length) // (len(text[i]) - 1)
            empty_1 = empty_n + (maxWidth - total_length) % (len(text[i]) - 1)
            count = 0
            for x in range(len(text[i]) - 1):
                count += 1
                if x == 0:
                    text[i].insert(x + 1, " " * empty_1)
                else:
                    text[i].insert(x + 1 * count, " " * empty_n)
    print(text)
    for i in text:
        print("".join(i))


text_justification(words, maxWidth)
