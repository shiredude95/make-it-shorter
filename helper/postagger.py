def noun_check(tag):
    """

    :param tag: a string representing a POS-TAG
    :return: boolean if the given tag belongs to the noun class
    """
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def verb_check(tag):
    """

    :param tag: a string representing a POS-TAG
    :return: boolean if the given tag belongs to the verb class
    """
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def adverb_check(tag):
    """

    :param tag: a string representing a POS-TAG
    :return: boolean if the given tag belongs to the adverb class
    """
    return tag in ['RB', 'RBR', 'RBS']


def adj_check(tag):
    """

    :param tag: a string representing a POS-TAG
    :return: boolean if the given tag belongs to the adjective class
    """
    return tag in ['JJ', 'JJR', 'JJS']


def postag(tag):
    """

    :param tag: a string representing a POS-TAG
    :return: a character string representing the general class that the pos tag belongs to
    """
    if adj_check(tag):
        return 'a'
    elif noun_check(tag):
        return 'n'
    elif adverb_check(tag):
        return 'r'
    elif verb_check(tag):
        return 'v'
    else:
        return 'n'