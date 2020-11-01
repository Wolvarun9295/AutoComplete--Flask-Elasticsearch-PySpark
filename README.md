# AutoSuggestion and AutoCorrection using Flask, Elasticsearch and PySpark
This project shows the working of AutoSuggestion and AutoCorrection similar to how some websites suggest when a search query is typed in the search bar.

There are 2 ways in which this project has been made:

1. Using Completion Suggester with Mapping
2. Using Fuzzy Query without Mapping
#
## Prerequisites:
- Python3 (**less than Python3.8** to avoid compatibility issues)
```
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
```
- [**Java JDK8**](https://jdk.java.net/) (required for **Spark**) and [**JDK11**](https://jdk.java.net/) (required for **Elasticsearch**)
- [**Apache Spark**](https://spark.apache.org/downloads.html) (**v2.4.x** preferable to avoid compatibility issues) and also install the **PySpark** using pip
```
$ sudo pip3 install pyspark
```
- [**Elasticsearch**](https://www.elastic.co/downloads/elasticsearch) and also install **Elasticsearch** using pip
```
$ sudo pip3 install elasticsearch
```
- [**ES Hadoop jar**](https://www.elastic.co/downloads/hadoop)
- [**Movie Dataset**](https://datasets.imdbws.com/title.basics.tsv.gz) from **IMDb**.
#
## Steps to run the code
***To see how Ingestion of data in Elasticsearch using PySpark is done, checkout this repo - [Spark-Elasticsearch-5MilData](https://github.com/Wolvarun9295/Spark-Elasticsearch-5MilData)***
1. Since the dataset is in tar.gz format, we have to untar it first using:
```
$ gunzip file.tar.gz
```
2. First add your dataset path in the **dataToES.py** file and run to ingest the data in Elasticsearch. Running this file will first clean the data and then ingest the data to the index.

    **NOTE:** If running the Completion Suggester option, the cleaned data will be stored in a folder named **movies_clean_dataset**  and it will create an index with the **Completion Suggester** mapping.
```
$ python3 dataToES.py
```
3. Finally, run the **run.py** file and access the landing page on **localhost:5000** if running on Local System or on **0.0.0.0:5000** if running on AWS or GCP.
```
$ python3 run.py
```

**Directory Sturcture of the Flask App:**

<img src=Screenshots/dirStructure.png height=”100”>

**The following screenshot shows the working of this project:**

<img src=Screenshots/autocomplete.gif height=”100”>

#
## References
- [Create a autocomplete System in Elastic Search | Frontend + Backend - soumilshah1995](https://youtu.be/gDOu_Su1GqY)
- [Elasticsearch Suggesters](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-suggesters.html#phrase-suggester)
- [Elasticsearch: Using Completion Suggester to build AutoComplete](https://medium.com/@taranjeet/elasticsearch-using-completion-suggester-to-build-autocomplete-e9c120cf6d87)
- [How To Map An Elasticsearch Index Using The Python Client](https://kb.objectrocket.com/elasticsearch/how-to-map-an-elasticsearch-index-using-the-python-client-266)
- [jQuery Autocomplete params](https://github.com/devbridge/jQuery-Autocomplete)
- [Jquery Autocomplete matching multiple unordered words in a string
](https://stackoverflow.com/questions/19084976/jquery-autocomplete-matching-multiple-unordered-words-in-a-string)
- [Spark: Saving file csv](https://www.edureka.co/community/47267/spark-saving-file-csv)
- [My question on StackOverflow](https://stackoverflow.com/questions/64588218/jquery-autocomplete-ajax-not-working-for-autocorrection-when-wrong-input-is-give)

#
## License and Copyright

© Varun I. Nagrare

Licensed under the [MIT License](LICENSE)