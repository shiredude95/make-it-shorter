import nltk
import math
from helper import constants


def scoreIDF1(all_tokens, num_sentences):
    """

    :param all_tokens:list of strings representing the tokens obtained from all
     the processed sentences
    :param num_sentences: integer representing the number of sentences
    remaining after preprocessing
    :return: a dictionary {string:float} k,v pair representing a word and its respective idf score
        calculated according to smooth idf and a list of most common words
    """
    fdist = nltk.FreqDist(all_tokens)

    # dictionary to maintian the idf scores of words
    idf_dict = {}
    for word in all_tokens:
        idf_dict[word] = math.log(1 + (num_sentences / fdist[word]), 2)
    # idf_dict[word] = fdist[word] / num_sentences
    most_common_words = list(fdist.most_common(constants.MOST_COMMON_COUNT))
    return idf_dict, most_common_words


def scoreIDF2(all_tokens, num_sentences):
    """

    :param all_tokens:list of strings representing the tokens obtained from all
     the processed sentences
    :param num_sentences: integer representing the number of sentences
    remaining after preprocessing
    :return:  a dictionary {string:float} k,v pair representing a word and its respective idf score
        calculated according to custom heuristic and a list of most common words
    """
    fdist = nltk.FreqDist(all_tokens)

    #dictionary to maintian the idf scores of words
    idf_dict = {}
    for word in all_tokens:
        # idf_dict[word]=math.log(1+(num_sentences/fdist[word]),2)
        idf_dict[word] = fdist[word] / num_sentences
    most_common_words = list(fdist.most_common(constants.MOST_COMMON_COUNT))
    return idf_dict, most_common_words
