def mock(s):
    n = True
    mock_lst = []
    for x in list(s):
        if x == ' ':
            n = False
        if n:
            mock_lst.append(x.lower())
            n = False
        else:
            mock_lst.append(x.upper())
            n = True
    return ''.join(mock_lst)

def spaced(s):
    spaced_lst = []
    for x in list(s):
        spaced_lst.append(x + ' ')
    return ''.join(spaced_lst)
