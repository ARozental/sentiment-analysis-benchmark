import json
import csv
import urllib2
import urllib
import requests
import time

from settings import *


def rate_limit(max_per_second):
    min_interval = 1.0 / float(max_per_second)

    def decorate(func):
        last_time_called = [0.0]

        def rate_limited_function(*args, **kargs):
            elapsed = time.clock() - last_time_called[0]
            left_to_wait = min_interval - elapsed
            if left_to_wait > 0:
                time.sleep(left_to_wait)
            ret = func(*args, **kargs)
            last_time_called[0] = time.clock()
            return ret
        return rate_limited_function
    return decorate


# MONKEYLEARN

def classify_text_monkeylearn(text_list, dataset_name):
    data = {
        'text_list': text_list
    }

    endpoint = {"generic": CLASSIFY_ENDPOINT_MONKEYLEARN,
                "airlines": CLASSIFY_ENDPOINT_MONKEYLEARN_AIRLINES,
                "apple": CLASSIFY_ENDPOINT_MONKEYLEARN_APPLE,
                "products": CLASSIFY_ENDPOINT_MONKEYLEARN_PRODUCTS,
                }

    response = requests.post(
        endpoint[dataset_name],
        data=json.dumps(data),
        headers={'Authorization': 'Token ' + API_KEY_MONKEYLEARN,
                 'Content-Type': 'application/json'}
    )
    return response.json()['result']


def classify_csv_monkeylearn(file_name, dataset_name):
    f = open(file_name)
    new_rows = []
    rows = [row for row in csv.reader(f)]
    batch_size = 200
    for i in xrange(0, len(rows), batch_size):
        res = classify_text_monkeylearn([row[0] for row in rows[i:i + batch_size]], dataset_name)
        for j, elem in enumerate(res):
            new_rows.append(rows[i + j] + [elem[-1]['label']])

    f.close()
    f = open('results/test_' + dataset_name + '_tagged_monkeylearn.csv', 'w')
    csv.writer(f).writerows(new_rows)
    f.close()


# METAMIND

# adjust rate limits to your plan (default free rate limit)
@rate_limit(1)
def classify_text_metamind(text):
    data = {
        "classifier_id": 155,
        "value": text
    }

    response = requests.post(
        CLASSIFY_ENDPOINT_METAMIND,
        data=json.dumps(data),
        headers={'Authorization': 'Basic ' + API_KEY_METAMIND,
                 'Content-Type': 'application/json'}
    )
    return response.json()


def classify_csv_metamind(file_name, dataset_name):
    f = open(file_name)
    new_rows = []
    for i, row in enumerate(csv.reader(f)):
        print i
        try:
            res = classify_text_metamind(row[0])
            label = res['predictions'][0]['class_name']
        except:
            print res
            label = 'NONE'
        new_rows.append(row + [label])
    f.close()

    f = open('results/test_' + dataset_name + '_tagged_metamind.csv', 'w')
    writer = csv.writer(f)
    writer.writerows(new_rows)
    f.close()


# ALCHEMY

def classify_text_alchemy(text, contextualize='false'):
    parameters = {
        'text': text,
        'apikey': API_KEY_ALCHEMY,
        'outputMode': "json"
    }
    url = CLASSIFY_ENDPOINT_ALCHEMY + urllib.urlencode(parameters)
    content = urllib2.urlopen(url).read()
    return json.loads(content)


def classify_csv_alchemy(file_name, dataset_name):
    f = open(file_name)
    new_rows = []
    for i, row in enumerate(csv.reader(f)):
        print i
        try:
            res = classify_text_alchemy(row[0])
            label = res['docSentiment']['type']
        except:
            print res
            label = 'NONE'
        new_rows.append(row + [label])
    f.close()

    f = open('results/test_' + dataset_name + '_tagged_alchemy.csv', 'w')
    csv.writer(f).writerows(new_rows)
    f.close()


# AYLIEN

# adjust rate limits to your plan (default free rate limit)
@rate_limit(1)
def classify_text_aylien(text):
    parameters = {"text": text}
    headers = {
        "Accept":                             "application/json",
        "Content-type":                       "application/x-www-form-urlencoded",
        "X-AYLIEN-TextAPI-Application-ID":    APPLICATION_ID_AYLIEN,
        "X-AYLIEN-TextAPI-Application-Key":   APPLICATION_KEY_AYLIEN
    }
    opener = urllib2.build_opener()
    request = urllib2.Request(CLASSIFY_ENDPOINT_AYLIEN, urllib.urlencode(parameters), headers)
    response = opener.open(request)
    return json.loads(response.read())


def classify_csv_aylien(file_name, dataset_name):
    f = open(file_name)
    new_rows = []
    for i, row in enumerate(csv.reader(f)):
        print i
        try:
            res = classify_text_aylien(row[0])
            label = res["polarity"]
        except Exception as e:
            print e
            label = 'NONE'
        new_rows.append(row + [label])
    f.close()

    f = open('results/test_' + dataset_name + '_tagged_aylien.csv', 'w')
    csv.writer(f).writerows(new_rows)
    f.close()


# HP IDOL

def classify_text_idol(text):
    params = {
        'text': text,
        'apikey': API_KEY_IDOL,
        'language': 'eng'
    }
    res = requests.get(CLASSIFY_ENDPOINT_IDOL, params=params)
    return res.json()


def classify_csv_idol(file_name, dataset_name):
    f = open(file_name)
    new_rows = []
    for i, row in enumerate(csv.reader(f)):
        print i
        try:
            res = classify_text_idol(row[0])
            label = res['aggregate']['sentiment']
        except:
            print res
            label = 'NONE'
        new_rows.append(row + [label])
    f.close()

    f = open('results/test_' + dataset_name + '_tagged_idol.csv', 'w')
    csv.writer(f).writerows(new_rows)
    f.close()


# DATUMBOX

def classify_text_datumbox(text):
    data = {
        'api_key': API_KEY_DATUMBOX,
        'text': text
    }
    return requests.post(CLASSIFY_ENDPOINT_DATUMBOX, data=data).json()


def classify_csv_datumbox(file_name, dataset_name):
    f = open(file_name)
    new_rows = []
    for i, row in enumerate(csv.reader(f)):
        print i
        try:
            res = classify_text_datumbox(row[0].replace('@', ' '))
            label = res['output']['result']
        except:
            label = 'NONE'
        new_rows.append(row + [label])
    f.close()

    f = open('results/test_' + dataset_name + '_tagged_datumbox.csv', 'w')
    csv.writer(f).writerows(new_rows)
    f.close()


if __name__ == "__main__":

    api_name = 'monkeylearn'
    dataset_name = "generic"

    file_name = 'data/test_' + dataset_name + '.csv'
    print "Classifying with " + api_name + "..."

    start_time = time.time()
    locals()["classify_csv_" + api_name](file_name, dataset_name)
    print("--- %s seconds ---" % (time.time() - start_time))

