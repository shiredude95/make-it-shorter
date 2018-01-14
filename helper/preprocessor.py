import re
from helper import stopwordslist, constants


def base_preprocess(raw):
    """

    :param raw: string represents the raw selected text
    :return: the processed raw string
    """
    ret = raw.lower() \
        .replace("\r", " ") \
        .replace("\n", " ") \
        .replace("&", " and ") \
        .replace("“", " ") \
        .replace("”", " ") \
        .replace('"', " ")
    ret = re.sub(r'[ ]{2,}', ' ', ret)
    return ret


def pre_process(tokenized_sents):
    """

    :param tokenized_sents: list of strings represents the tokenized sentences
    :return: 2 dictionaries both {int:string} with the first
    representing a key value pair of an index and a pre_processed
    string and the second dictionary representing a key value pair of an
    index and base_preprocessed string.
    """
    count = 0

    #dictionary {int:string} key value pair with key representing an index
    # and string representing a a preprocessed string
    mapped_lines = {}

    #dictionary {int:string} key value pair with key representing an index
    # and string representing a a base processed string
    actual_lines = {}

    # loop through the tokenized sentences
    for tokenized_sent in tokenized_sents:
        actual_lines[count] = tokenized_sent

        # agressive yet fast way of dealing with plurals
        tokenized_sent = tokenized_sent.replace("’", "'").replace("'s"," ")

        #regex to remove all terms with anything other than a character in it
        char_regex = re.compile(r'[^a-zA-Z ]')
        tokenized_sent = char_regex.sub('', tokenized_sent)
        tokenized_sent = re.sub(r'[ ]{2,}', ' ', tokenized_sent)

        # only selecting those words to calculate the score that have greater
        # length than WORD_LENGTH_THRESHOLD,
        tokenized_sent = " ".join(str(x) for x in tokenized_sent.split(" ") if
                        len(x) > constants.WORD_LENGTH_THRESHOLD
                        and not x in stopwordslist.list_stopwords)

        #filter out all the sentences that do not clear SENTENCE_WORDS_THRESHOLD
        if len(tokenized_sent.split(" ")) < constants.SENTENCE_WORDS_THRESHOLD:
            continue

        #assign an index to the processed tokenized sent
        mapped_lines[count] = tokenized_sent.strip()
        count += 1
    return mapped_lines, actual_lines
