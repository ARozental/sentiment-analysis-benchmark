import csv

dataset = "generic"
# dataset = "products"
# dataset = "apple"
# dataset = "airlines"

print "Test results for:", dataset

for api_name in ['monkeylearn', 'metamind', 'alchemy', 'aylien', 'idol', 'datumbox']:
    f = open('results/test_' + dataset + '_tagged_' + api_name + '.csv')
    rows = [row for row in csv.reader(f)]
    total = 0
    correct = 0

    total_positive = 0
    correct_positive = 0
    total_predicted_positive = 0

    total_negative = 0
    correct_negative = 0
    total_predicted_negative = 0

    total_neutral = 0
    correct_neutral = 0
    total_predicted_neutral = 0

    for row in rows:
        total += 1
        if row[1] == row[2]:

            correct += 1

            if row[1] == "positive":
                total_positive += 1
                correct_positive += 1
                total_predicted_positive += 1
            elif row[1] == "negative":
                total_negative += 1
                correct_negative += 1
                total_predicted_negative += 1
            else:
                total_neutral += 1
                correct_neutral += 1
                total_predicted_neutral += 1

        else:
            if row[1] == "positive":
                total_positive += 1
            elif row[1] == "negative":
                total_negative += 1
            else:
                total_neutral += 1

            if row[2] == "positive":
                total_predicted_positive += 1
            elif row[2] == "negative":
                total_predicted_negative += 1
            else:
                total_predicted_neutral += 1

    print

    print api_name, ',accuracy,', '%.4f' % (correct * 1.0 / total)

    print api_name, ',recall positive,', '%.4f' % (correct_positive * 1.0 / total_positive)
    print api_name, ',precision positive,', '%.4f' % (correct_positive * 1.0 / total_predicted_positive)

    print api_name, ',recall negative,', '%.4f' % (correct_negative * 1.0 / total_negative)
    print api_name, ',precision negative,', '%.4f' % (correct_negative * 1.0 / total_predicted_negative)

    print api_name, ',recall neutral,', '%.4f' % (correct_neutral * 1.0 / total_neutral)
    print api_name, ',precision neutral,', '%.4f' % (correct_neutral * 1.0 / total_predicted_neutral)

    print




