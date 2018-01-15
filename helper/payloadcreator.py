from helper import preprocessor, constants, shortmaker
from nltk import data


def get_payload(request):

    """

    :param request: HTTP request
    :return: A Dictionary {string:object} key,value pair
    """

    small_summary = False
    lemma_flag = False

    raw = request.form['text']
    small_summary_string = request.form['summarySize']
    lemma_flag_string = request.form['lemmaFlag']

    if small_summary_string == "true":
        small_summary = True
    if lemma_flag_string == "true":
        lemma_flag = True

    # do some preliminary processing on the raw selected text
    raw = preprocessor.base_preprocess(raw)

    # cached automatically by nltk,so no reason to exteranlly cache it
    sent_detector = data.load('tokenizers/punkt/english.pickle')

    # tokenize the raw text into sentences and filter out sentences with
    # less than SENTENCE_WORDS_THRESHOLD words
    tokenized_sents = sent_detector.tokenize(raw)
    tokenized_sents = [sent for sent in tokenized_sents if
                       len(sent.strip().split(
                           ' ')) > constants.SENTENCE_WORDS_THRESHOLD]
    if len(tokenized_sents) > constants.NUM_SENTS_THRESHOLD:
        (processed_lines, actual_lines) = preprocessor \
            .pre_process(tokenized_sents)

        payload = shortmaker \
            .makeshort(processed_lines, actual_lines, small_summary, lemma_flag)
        return payload
    else:
        payload = {}
        payload["Error"] = "Selection too short. No Summary generated."
        return payload
