def single_root_words(root_word, *other_words):
    same_words = []
    root_lower = root_word.lower()
    for s in other_words:
        if root_lower in s.lower() or s.lower() in root_lower:
            same_words.append(s)
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')