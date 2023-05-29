# datafun-03-discussion

## Recommended

- VS Code Editor (for scripts and notebooks)

## Set Up Virtual Environment

In VS Code, open a Terminal / New Terminal and run the following. 
This will create a virtual environment in the .venv folder and install the required packages.
The commands are for Windows and PowerShell. Slight adjustments may be needed for other environments.
Click Yes when VS Code asks about the environment. 
Allow some time for the installations to complete before running the code.

```shell
python -m pip install --upgrade pip 
python -m venv .venv
.venv\Scripts\Activate
python -m pip install --upgrade pip ipykernel jupyterlab wordcloud matplotlib
python -m ipykernel install --user --name .venv --display-name "Python (.venv)"
```

Note: If `python` doesn't work, replace it with `py` or `python3`.

## Run The Code

Run the script from the command line:

```shell
python learning.py
```

Or open the notebook [learning.ipynb](./learning.ipynb). 
Select Kernel / Python Environment / Python (.venv) from the menu.
Then run the cells.


## Exploratory Data Analysis in Daily Life

In our third discussion, we asked:

- Which learning resources do you prefer/find most effective?

One way to gain insight is to turn the discussion into a word cloud.

## Questions

- How well did this process work?
- Could you add a third chart - or other analysis - to help gain insights?

## Insights

![Initial wordcharts](./output.png)
