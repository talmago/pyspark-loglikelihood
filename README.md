# pyspark-loglikelihood
PySpark Loglikelihood Examples.

Inspired by [Mahout](http://mahout.apache.org/):
* [LogLikelihood](https://github.com/apache/mahout/blob/master/math/src/main/java/org/apache/mahout/math/stats/LogLikelihood.java)
* [User / Item Similarity](https://github.com/apache/mahout/blob/master/mr/src/main/java/org/apache/mahout/cf/taste/impl/similarity/LogLikelihoodSimilarity.java)
* [Nearest N-Neighborhood](https://github.com/apache/mahout/blob/master/mr/src/main/java/org/apache/mahout/cf/taste/impl/neighborhood/NearestNUserNeighborhood.java) 


### Installation

```sh
$ pip install https://github.com/talmago/pyspark-loglikelihood/archive/master.zip
```

> **NOTICE:** PySpark Loglikelihood is adapted to [python2.7](https://www.python.org/download/releases/2.7/) to run. [pyenv](https://github.com/yyuu/pyenv) and [virtualenv](https://virtualenv.pypa.io/en/stable/) are recommended for setting an independent python environment.


### Usage

After the installation you can use `spark-submit` command line to execute the item-similarity and user-similarity jobs with your dataset respectively.


#### Item-Item Similarity (LogLikelihood)

```sh
$ spark-submit item_similarity.py \
               input.csv \
               output \
               --maxPrefs=10000 \
               --maxSimilaritiesPerItem 100
```
> **NOTICE:** Input file lines are expected to be comma seperated vectors of `USER_ID`,`ITEM_ID`. Output format will be consisted of `ITEM_ID1`,`ITEM_ID2`,`SCORE`.


#### User-User Similarity (N-neighborhood + Loglikelihood)

```sh

$ spark-submit user_similarity.py \
               input.csv \
               output \
               --numOfNeighbors=40 \
               --numOfRecommendations 1000
```
> **NOTICE:** Input file lines are expected to be comma seperated vectors of `USER_ID`,`ITEM_ID`. Output format will be consisted of `USER_ID`,`ITEM_ID`,`SCORE`.

### Example

##### Run [exmple](https://github.com/talmago/pyspark-loglikelihood/blob/master/examples/item-similarity-ml-100k-dataset) from command line

```sh
wget -O - https://raw.githubusercontent.com/talmago/pyspark-loglikelihood/master/examples/item-sim-ml-100l-dataset | bash -x
```

##### Step by Step

Step 1: Download and re-format the [movielens 100k](https://grouplens.org/datasets/movielens/100k/) dataset.

```sh
$ wget -O - http://files.grouplens.org/datasets/movielens/ml-100k/u.data | cut -f1 -f2 | tr '\t' ',' > input.csv
```

Step 2: Upload data set to local hfds

```sh
$ hadoop fs -rm -r /item-sim
$ hadoop fs -mkdir -p /item-sim
$ hadoop fs -moveFromLocal input.csv /item-sim/input.csv
```

Step 3: Run item-silmilarity job on our hadoop data set

```sh
$ spark-submit item_similarity.py \
               /item-sim/input.csv \
               /item-sim/output \
               --maxPrefs=10000 \
               --maxSimilaritiesPerItem 100
```

Step 4: Merge parquet files into a single csv file

```sh
$ hadoop fs -getmerge /item-sim/output result.csv
```

Step 5: Analyze / process / visualize the result set

```sh
$ head result.csv
26,381,0.9889748
26,732,0.9876871
26,70,0.98738647
26,715,0.98685825
26,238,0.98625606
26,58,0.98580784
26,1,0.985786
26,83,0.9857064
26,88,0.9856318
26,367,0.9854448
```
