def cut_sent(words):
    start = 0
    i = 0
    sents = []
    punt_list = '。！？'
    for word in words:
        if word in punt_list:
            sents.append(words[start:i+1])
            start = i + 1
            i += 1
        else:
            i += 1
    if start < len(words):
        sents.append(words[start:])
    return sents

