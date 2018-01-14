import operator
from math import floor
from helper import constants


def create_nths_bucket(index_tfidf_map):
    """

    :param index_tfidf_map:dictionary, {int:float} key,value pair with the keys
     representing the index of the sentence and the value representing its
     tf-idf score
    :return: a list of integers representing the top ranked sentence
    (by tfidf score) in each of the NUM_BUCKETS buckets
    """
    nths_top_list = []
    total_lines = len(index_tfidf_map)

    # set number of breakpoints at whiich you want to create a bucket
    num_breakpoints = floor(total_lines / constants.NUM_BUCKETS)

    break_point_limit = int(num_breakpoints * constants.NUM_BUCKETS)

    # loop to select the top ranking sentence from each of the buckets
    for i in range(0, break_point_limit, constants.NUM_BUCKETS):
        nths_top_list.append(
            max(list(index_tfidf_map.items())[i:i + constants.NUM_BUCKETS],
                key=operator.itemgetter(1))[0])

    # condition to select the top ranking sentence from the last possibly
    # unevenly sized bucket
    if break_point_limit <= total_lines:
        nths_top_list.append(
            max(list(index_tfidf_map.items())[break_point_limit - 1:],
                key=operator.itemgetter(1))[0])
    return nths_top_list


def create_top_n_bucket(index_tfidf_map):
    """

    :param index_tfidf_map: dictionary, {int:float} key,value pair with the keys
     representing the index of the sentence and the value representing its
     tf-idf score
    :return: a list of integers representing the top n ranked (by tfidf scores)
     sentences from all of the given indexed sentences
    """
    top_n_list = []
    total_lines = len(index_tfidf_map)

    # setting the N value in top N
    topN = round(total_lines / constants.NUM_BUCKETS)

    # sort the indexed sentences by tfidf scores
    sorted_tf_idf = sorted(index_tfidf_map.items(), key=operator.itemgetter(1),
                           reverse=True)

    # adding the topN sentences to the returning list
    for i in range(0, topN):
        top_n_list.append(sorted_tf_idf[i][0])

    return top_n_list
