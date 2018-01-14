from helper import tfscorer, idfscorer, bucketmaker, tfidfscorer


# in readme add that ive used customized version of tfidf
# this is because i believe an article is inherently differeent to a corpus
# maybe add softmax
# add comments to all the functions
# upload apna crawler to github
# beta test bigrams

def makeshort(processed_lines_map, actual_lines_map, smallSummary,lemmaFlag):
    """

    :param processed_lines_map:dictionary {int:string} representing
     a key value pair of an index and a further modified string
    :param actual_lines_map:dictionary {int:string} representing
     a key value pair of an index and base_preprocessed string.
    :return: dictionary {string:Object} with key value pair
    representing a key string and the objects representing a list of
    summary lines,summary ratio and a list of most common words mapped
    according to their key string.

    """
    num_actual = len(actual_lines_map)
    num_processed = len(processed_lines_map)


    payload = {}
    summary_lines = [] # list of summarized lines according to the ranking algorithm
    fifths_map1 = [] #list of top ranked sentence every N th bucket
    top_n_map1 = [] #list of top N ranked sentence indices

    # send for tf for sent
    all_tokens, words_tf = tfscorer.scoreTF(processed_lines_map,lemmaFlag)

    #only if user has selected normal summary option
    if not smallSummary:

        # send for idf for words according to smooth idf (method#1)
        words_idf1, most_common_words = idfscorer.scoreIDF1(all_tokens,
                                                            num_processed)
        # tfidf score according to (method#1)
        tf_idf1 = tfidfscorer.scoreTFIDF(processed_lines_map, words_tf,
                                         words_idf1)

        # summary lines according to method#1
        fifths_map1 = bucketmaker.create_nths_bucket(tf_idf1)
        top_n_map1 = bucketmaker.create_top_n_bucket(tf_idf1)


    # send for idf for words according to custom heuristic (method#2)
    words_idf2, most_common_words = idfscorer.scoreIDF2(all_tokens,
                                                        num_processed)

    # tfidf score according to (method#2)
    tf_idf2 = tfidfscorer.scoreTFIDF(processed_lines_map, words_tf, words_idf2)

    # summary lines according to method#2
    fifths_map2 = bucketmaker.create_nths_bucket(tf_idf2)
    top_n_map2 = bucketmaker.create_top_n_bucket(tf_idf2)

    # get the unique sentences from the summary lines
    summary_index_set = set(fifths_map1 + fifths_map2 + top_n_map1 + top_n_map2)
    summary_index_set.add(0)
    summary_index_set.add(num_processed - 1)

    # sort the sentences according to their index
    summary_index_list = sorted(summary_index_set)

    # loop through the summary indices to add them to the summary lines list
    for index in summary_index_list:
        summary_lines.append(actual_lines_map[index].strip()
                             .capitalize()
                             .replace(" i ", " I "))

    # calculate the summary ratio
    shorter_ratio = (len(summary_index_list) / num_actual) * 100
    shorter_effect = 100 - shorter_ratio

    # build the payload
    payload["summaryLines"] = summary_lines
    payload["reducedBy"] = shorter_effect
    payload["mostCommonWords"] = most_common_words

    return payload
