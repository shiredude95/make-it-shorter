import nltk
from helper import postagger, stopwordslist


def tf_sent(tokens_in_sent):
    """

    :param tokens_in_sent: list of tokens in sentence
    :return: a dictionary, {string:int} key,value pair representing a
     word and its respective normalized term frequency
    """
    fdist = nltk.FreqDist(tokens_in_sent)
    len_sent = len(tokens_in_sent)
    word_tf_in_sent = {}
    for word in tokens_in_sent:
        tf = fdist[word] / len_sent
        word_tf_in_sent[word] = tf
    return word_tf_in_sent


def lemmatize(tokens_in_sent):
    """

    :param tokens_in_sent: list of tokens in a sentence
    :return: the lemmatized versions of the given tokens
    """
    sentence_postags = nltk.pos_tag(tokens_in_sent)
    sentence_lemma_list = [
        nltk.stem.WordNetLemmatizer().lemmatize(word, postagger.postag(postype))
        for (word, postype) in sentence_postags
        if (
            postype.startswith('CD')
            or postype.startswith('FW')
            or postype.startswith('J')
            or postype.startswith('LS')
            or postype.startswith('N')
            or postype.startswith('R')
            or postype.startswith('U')
            or postype.startswith('V')
        )]

    final_lemmas = [lemma for lemma in sentence_lemma_list
                    if len(lemma) > 2 and lemma
                    not in stopwordslist.list_stopwords]
    return final_lemmas


def scoreTF(processed_lines, lemmatize_flag):
    """

    :param processed_lines: list of lines that have been pre_processed
    :param lemmatize_flag: boolean represents if the user has selected the lemmatize
     option
    :return: a list of tokens from all the given lines in the list
     and a dictionary {int:dict} representing a k,v pair of an index (key) and a
     dictionary of {string:int} (value) representing the words and their respective
     frequencies in the sentence in the respective index.
    """
    words_tf = {}
    all_tokens = []
    for sentence_index in processed_lines.keys():
        tokens_in_sent = processed_lines[sentence_index].split(" ")

        if lemmatize_flag:
            final_lemmas = lemmatize(tokens_in_sent)
            all_tokens.extend(final_lemmas)
            words_tf[sentence_index] = tf_sent(final_lemmas)

        else:
            all_tokens.extend(tokens_in_sent)
            # calculate tfscore for each sentence
            words_tf[sentence_index] = tf_sent(tokens_in_sent)

    return all_tokens, words_tf
