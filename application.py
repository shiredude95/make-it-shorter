from nltk import data
from flask import Flask, request, render_template
from helper import preprocessor, shortmaker, constants

application = Flask(__name__)


@application.route('/shorter', methods=['POST', 'GET'])
def shorter():
    """

    :return:renders the template with the summary of text obtained from the
     selection
    """
    if request.method == 'POST':
        smallSummary = False
        lemmaFlag = False

        raw = request.form['text']
        smallSummaryString=request.form['summarySize']
        lemmaFlagString = request.form['lemmaFlag']


        if smallSummaryString=="true":
            smallSummary=True
        if lemmaFlagString=="true":
            lemmaFlag=True


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
                .makeshort(processed_lines, actual_lines,smallSummary,lemmaFlag)

            return render_template('render.html', render_payload=payload)
        else:
            payload = {}
            payload["Error"] = "Selection too short. No Summary generated."
            return render_template('render.html', render_payload=payload)
    else:
        return render_template('welcome.html')


@application.route('/')
def welcome():
    """

    :return: renders the welcome template
    """
    return render_template('welcome.html')


if __name__ == '__main__':
    application.debug = True
    application.run(host='localhost', debug=True)
