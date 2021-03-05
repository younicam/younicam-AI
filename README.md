# younicam-AI

Machine Learning project developed in PySpark. The ML model uses the dataset related to the anonymized presences registered via the Younicam mobile application in the University of Camerino's buildings to predict the number of people in a room during a precise time interval.

[TPOT](https://epistasislab.github.io/tpot/) is used in the model training phase to get the best combination between the ML model and hyperparameters.

## Get started

### Prerequisites

* [Python](https://www.python.org/downloads/)
* [Apache Spark](https://spark.apache.org/downloads.html)
* [Jupyter](https://jupyter.org/install)
* [PySpark](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)

Under your home directory, find a file named .bash_profile, .bashrc or .zshrc. This name might be different according to the operation system or version. After that, open the bash shell startup file and past the script below:

```bash
export SPARK_HOME="/opt/spark"
export PATH="$SPARK_HOME/bin:$PATH"
```

If you want Jupyter Notebook to be opened when launching PySpark, add also the variables below:

```bash
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS=notebook
```

Now you are able to launch PySpark from any directory with the underneath command:

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

Launch PySpark, as described above, and browse into the project directory to execute the notebooks.

If the Jupyter Notebook doesn't open automatically with PySpark, open it using the command below:

```bash
jupyter notebook /path/to/notebook
```

The *TPOT pipeline* notebook was used in order to find the best combination between ML model and hyperparameters. It outputs a .py pipeline to run the selected ML model with its configurations. We used the returned pipeline inside the *Model Training* notebook in order to perform additional operation around the training (e.g. save intermediate dataset, evaluation).

## Structure

The repository has the following folder structure:

* *data* : contains the original dataset plus some other intermediary transformations in json format
* *notebooks* : contains all the notebooks used during experimentation. There are a notebook for the collection and preparation phases, one for the training and evaluation phases, one for the predictions visualization and another one to execute the TPOT pipeline.
* *predictions* : contains the final predictions results in csv format

## Authors

* **Yuri Paoloni** - [yuripaoloni](https://github.com/yuripaoloni)
* **Matteo Leonesi** - [MatteoLeonesi](https://github.com/MatteoLeonesi)
