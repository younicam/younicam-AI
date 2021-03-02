# younicam-AI

Machine Learning project developed in PySpark. The model uses the dataset related to the anonymized presences registered via the Younicam mobile application in the University of Camerino's buildings to predict the number of people in a room during a precise time interval.

[TPOT](https://epistasislab.github.io/tpot/) is used in the model training phase to get the best combination between the ML model and hyperparameters.
## Get started

### Prerequisites

* [Python](https://www.python.org/downloads/)
* [Apache Spark](https://spark.apache.org/downloads.html)
* [pip](https://pip.pypa.io/en/stable/installing/)
* [Jupyter](https://jupyter.org/install)

Install Pyspark:

```bash
pip install pyspark
```

Under your home directory, find a file named .bash_profile or .bashrc or .zshrc. This name might be different in different operation system or version. After that, open the bash shell startup file and past the script below:

```bash
export SPARK_HOME="/your/home/directory/spark/python"
export PATH="$SPARK_HOME/bin:$PATH"
```
Now you are able to launch PySpark from each directory with the following command:

```bash
pyspark
```

### Install dependencies 

To install the project dependencies run the following command:

```bash
pip install -r requirements.txt
```
Notice that the TPOT pipeline needs some additional dependencies listed in the [TPOT installation docs](https://epistasislab.github.io/tpot/installing/).

## Usage

Launch PySpark, as described above, and browse into the project directory to launch the notebooks.

If the Jupyter Notebook doesn't open automatically with PySpark, open it using the command below:

```bash
jupyter notebook /path/to/notebook
```

## Structure

The repository has the following structure:

* *data* : this folder contains the original dataset plus some other intermediary transformations
* *notebooks* : contains all the notebooks used during experimentation. There are a notebook for the collection and preparation phases, one for the training and evaluation phases and another one to execute the TPOT pipeline.
* *predictions* : contains the final predictions results in csv format

## Authors

* **Yuri Paoloni** - [yuripaoloni](https://github.com/yuripaoloni)
* **Matteo Leonesi** - [MatteoLeonesi](https://github.com/MatteoLeonesi)
