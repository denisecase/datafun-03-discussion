# Publish to Google Colab

Run your Jupyter notebooks interactively via Google Colab.

## Steps to open a notebook on Google Colab:

1. Upload your Jupyter notebook (*.ipynb) to a GitHub repository.
2. Navigate to Google Colab at `https://colab.research.google.com/`.
3. Click on `File` in the upper left corner, then click `Open notebook`.
4. In the window that opens, click on the `GitHub` tab. 
5. Search for the GitHub repository where your notebook is stored.
6. Once you've located your repository, click on it, then click on the notebook file you wish to open.

## Directly open a notebook in Google Colab:

Alternatively, you can directly open a notebook in Google Colab from GitHub by changing the URL.
Change from GitHub to Colab as follows:

- https://github.com/username/repository/blob/main/notebook.ipynb
- https://colab.research.google.com/github/username/repository/blob/main/notebook.ipynb

Replace username, repository, and notebook.ipynb with your GitHub username, your repository name, and your notebook filename, respectively.
This will open your notebook directly in Google Colab. Example: 

- https://github.com/denisecase/datafun-03-discussion/blob/main/learning.ipynb
- https://colab.research.google.com/github/denisecase/datafun-03-discussion/blob/main/learning.ipynb

## Google Colab

Google Colab provides a Python environment, so any libraries you want to use in your notebook must be installed first. You can install libraries using `%pip install library_name` directly in a notebook cell.

Google Colab does not persistently store the installed libraries 
or any data you might upload or generate. Everything will be reset once you close the session. 
If your notebook requires data files, you might need to upload them manually, 
or you can use Google Drive to store and access them.

The `%` syntax is a part of IPython's magic commands. 
These are special commands for Jupyter that are not part of standard Python syntax. 
You can read more about them [here](https://ipython.readthedocs.io/en/stable/interactive/magics.html).
The `%pip install` command works because Jupyter notebooks run an IPython kernel behind the scenes, 
which supports these magic commands. 
If you try to run the same command in a standard Python interpreter, it may result in a syntax error.