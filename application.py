from nltk import data
from flask import Flask, request, render_template
from helper import payloadcreator
import json

application = Flask(__name__)

data.path.append('/libs/nltk_data/')




@application.route('/shorter', methods=['POST', 'GET'])
def shorter():
    """

    :return:renders the template with the summary of text obtained from the
     selection
    """
    if request.method == 'POST':



        #obtain the payload which is a dictionary of {string:object} k,v pair
        payload = payloadcreator.get_payload(request)

        mobileFlag= request.form['mobile']

        if mobileFlag=="true":
            return json.dumps(payload)
        else:
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
    # application.debug = True
    application.run()
