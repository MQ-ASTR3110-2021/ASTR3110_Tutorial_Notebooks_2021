# Google Colab Setup

Most tutorials will involve live-coding in Jupyter Notebooks hosted on
[Google
Colab](https://colab.google.com/). This
is a free cloud-based service that supports access to graphics
processing units (GPUs).

Storage space for data, code and output files is provided by linking
to your Google Drive. Please setup (or login to) a Google account
before taking the steps below. **NB: you must be logged into only
*one* Google account in your current browser session.** Make sure that
you have enough space on your Google Drive (check at
[http://drive.google.com](http://drive.google.com)).

## Step 1: Link Colab to your Google Drive

 * Go to the URL [https://colab.research.google.com](https://colab.research.google.com)
 * Log in to your Google account. 
 * Click on the New Python 3 notebook from the File menu to create a new notebook.
 * Add a code cell to the notebook with the following code:

```
from google.colab import drive
drive.mount('/content/gdrive')
```

 * Run the code cell to connect to your Google Drive.
 * Enter your authorization code from the provided link.

## Step 2: Download the tutorial materials to your Google Drive

Add another code cell to the notebook and run the following line of code:

```
cd gdrive/'My Drive'
```

Wait for this to execute successfully and then do the following in a
new cell:

```
!git clone https://github.com/MQ-ASTR3110-2020/ASTR3110_Tutorial_Notebooks.git
```

This clones (downloads) the tutorial materials from the GitHub online
repository. 

## Step 3: Start a Jupiter Notebook and reconnect to your Google Drive.

Most excercises in this tutorial are done within a Jupyter
Notebook. You can think of these as being similar to a spreadsheet
with a single column of cells, each of which contains a block of
code. You execute these blocks in sequence.

Each topic within the tutorial is contained in a dedicated notebook,
which will be added to the repository as the session progresses. When
starting a new Notebook session you will need to relink to your Google
Drive (if you need to save data from the Notebook):

 * Go to the URL https://www.google.com/drive/.
 * Log in to your Google account (if not already logged in).
 * Check you are in the correct Google account (top right corner of browser).
 * Open the directory where you downloaded the course content.
 * Open a notebook, e.g. ```ASTR3110_Tutorial_1_Probabilities.ipynb```, with Colaboratory.
 * Add a code cell at the top of the notebook with the code:
 
```
from google.colab import drive
drive.mount('/content/gdrive')
import os
os.chdir('./gdrive/My Drive/ASTR3110_Tutorial_Notebooks')
```
 * Enter your authorization code from the provided link again.

 * Run the code cell. Now, the notebook is ready for your experiment.

