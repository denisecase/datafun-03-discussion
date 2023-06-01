# Upload Your Data to Google Drive and Access It in Google Colab

## Uploading your file to Google Drive

1. Navigate to your Google Drive account.
2. Click on the "+ New" button on the left-hand side.
3. Select "File upload" and then select your `data.txt` file from your local system.

## Accessing Your Data in Google Colab or Locally

You can use the Python `os` module to determine the environment in which your code is running. 
Based on this, you can choose to read the file from Google Drive (if in Colab) or from the local file system.

```python
import os
from google.colab import drive

# Detect if this is running in Google Colab
if 'google.colab' in str(get_ipython()):
    print('Running on CoLab')
    drive.mount('/content/drive')
    file_path = '/content/drive/My Drive/data.txt'  # Modify this path to match the location of your file in Drive
else:
    print('Not running on CoLab')
    file_path = 'data.txt' 

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()
```



