from collections import OrderedDict
def scoreTFIDF(line_map, word_tfs, word_idfs):

    """

    :param line_map: a dictionary {index:string} representing aa k,v pair of
     an index and a string that represents a sentence with processed terms
    :param word_tfs: a dictionary {word:int} representing a k,v pair of a
      word and its frequency in a given indexed sentence
    :param word_idfs: a dictionary {word:float} representing a k,v pair of a
     word and its respective idf score
    :return: a dictionary {index:float} representing a k,v pair representing a
     sentence index and its respective tf-idf score.
    """

    #initialize an OrderedDict to guarantee order of the insertion is maintained
    # so we can implement our summarization heuristic
    tf_idf = OrderedDict()

    # loop through the index of the processed sentence indices
    for sentence_index in line_map.keys():

        #word_tf_map represents a dict of all the words and respective tf in
        # a sentence
        words_tf_map = word_tfs[sentence_index]
        tf_idf_val = 0

        #loop through the words in a sentence
        for word in words_tf_map.keys():

            tf_val = words_tf_map[word]
            idf_val = word_idfs[word]

            #calculate the tfidf score
            tf_idf_val += tf_val * idf_val

        #assign the tfidf score of a sentence
        tf_idf[sentence_index] = tf_idf_val
    return tf_idf