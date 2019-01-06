import os
from flask import Flask, render_template
import json
import pandas as pd
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, KeywordsOptions
app=Flask(__name__)
natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2018-03-16',
        iam_apikey='uadU0ugexoaWk7AzjFkltF0k7-ltbVF5L_UD_rAI3vLP',
        url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api'
)
port = int(os.getenv('PORT', 8000))
@app.route('/')
def home():
    # return render_template('try.html')
    return '<center> <h1>ok ! <br>The App is Running<h1> </center>'


@app.route('/ryu/')
def ryu():

    response = natural_language_understanding.analyze(text='  Define topology and explain the advantages and disadvantages of BUS  Discuss two dynamic routing algorithms with examples. What is congestion? Explain congestion control in datagram subnets. Discuss IEEE LAN standardsWhat are design issues of session layers? Discuss the various duties of session layer.',
    features=Features(keywords=KeywordsOptions(sentiment=False,emotion=False,limit=6))).get_result()
    d=response
    df=pd.DataFrame(d['keywords'])
    # af=pd.DataFrame.to_string(df)
    # return af
    return render_template("avi.html",data=df.to_html())
    # print(json.dumps(response, indent=4))
    # return 'hello'
    #return render_template("data_analysis.html",  data=x.to_html())

if __name__ == '__main__':
    app.run(port = port ,debug = True)

