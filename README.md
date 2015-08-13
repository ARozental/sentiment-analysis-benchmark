# Sentiment Analysis APIs Benchmark

Source code to run the sentiment analysis benchmark that compares the performance
of different NLP APIs predicting the sentiment on tweets.

You can read the full post [here](https://blog.monkeylearn.com/sentiment-analysis-apis-benchmark).

Different datasets were used for this benchmark:

- **Generic**: is a set of tweets with comments about celebrities, brands, movies and
products. The tweets were collected with Twitter API and tagged by humans using
[CrowdFlower](http://www.crowdflower.com/) platform.

The rest of the datasets are part of the [Crowdflower's data for everyone initiative](http://www.crowdflower.com/data-for-everyone):

- **Products & brands**: tweets with comments about multiple brands and products.
The full dataset can be accessed [here](http://cdn2.hubspot.net/hub/346378/file-549032717-csv/data/1377884607_tweet_product_company.csv?t=1434864711160).

- **Apple products**: tweets with comments about Apple products.
The full dataset can be accessed [here](http://cdn2.hubspot.net/hub/346378/file-2544425304-csv/DFE_CSVs/Apple-Twitter-Sentiment-DFE.csv?t=1434864711160).

- **Airlines**: tweets with comments about different US airlines.
The full dataset can be accessed [here](http://cdn2.hubspot.net/hub/346378/file-2545951097-csv/DFE_CSVs/Airline-Sentiment-2-w-AA.csv?t=1434864711160).

Scripts provided:

- **api_benchmarks.py** runs all the APIs classifications, just set the following variables
in the main script:

  - **api_name** = to the name of the API to run (monkeylearn, metamind, alchemyAPI
  - **dataset_name** = the name of the dataset to run ["generic", "products", "apple", "airlines"]

- **get_accuracies.py** calculates the accuracy, precision and recall of each category
(positive, neutral and negative). You must select the dataset to run the calculations
at the top of the script.

- **settings.py** before running the scripts, you must fill this file with your
tokens for each API.

