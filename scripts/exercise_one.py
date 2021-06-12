
def pattern_count(pattern1, pattern2):
    '''
    Count the times match both patterns within dataset

    Dotted quad values are strings of four u1 integer separated
        by dotes:

    e.g. 'Huffington Post' and 'https://mymagazine.pdf'

    Args:
        value (:obj:`str`): the value to be matched.

    Returns:
        :obj:`int`: times the patterns are matched
    '''
   
    import re
    pattern = pattern1
    countHuffington = 0
    patternUrl = re.compile(pattern2)
    countUrl = 0

    f = open('../data/covid_approval_polls.csv', 'r')
    for linea in f:
        for match in re.finditer(pattern, linea):
            countHuffington+=1
        for match in re.finditer(patternUrl, linea):
            countUrl+=1
    f.close
    # The pattern Huffington_Post appears X times.
    # The pattern url_pdf appears Y times.
    print('The pattern number 1 appears', countHuffington, 'times')
    print('The pattern number 2 appears', countUrl, 'times')
   
if __name__ == "__main__":
   
    import re
    pattern = 'Huffington Post'
    countHuffington = 0
    patternUrl = re.compile(r'''http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]\.pdf))''')
    countUrl = 0

    f = open('../data/covid_approval_polls.csv', 'r')
    for linea in f:
        for match in re.finditer(pattern, linea):
            countHuffington+=1
        for match in re.finditer(patternUrl, linea):
            countUrl+=1
    f.close
    # The pattern Huffington_Post appears X times.
    # The pattern url_pdf appears Y times.
    print('The pattern Huffington_Post appears', countHuffington, 'times')
    print('The pattern url_pdf appears', countUrl, 'times')