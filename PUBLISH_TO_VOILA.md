# Publish to Voilà 

Voilà and ipywidgets turn Jupyter notebooks into interactive web applications. 

## Install Voilà

**Deactivate** the virtual environment and 
install voila into your default Python environment. 

```shell
deactivate
python -m pip install --upgrade voila
```

## Run Voilà and View Notebook

Once installed, you can run `voila` in the terminal followed by the path to your notebook file. 
It will open <http://localhost:8866/> in your browser.

```shell
voila learning.ipynb 
```

## Publish to Voilà Using Binder

Follow the instructions at [PUBLISH_TO_BINDER.md](./PUBLISH_TO_BINDER.md).
Modify them as described [here](https://voila.readthedocs.io/en/latest/deploy.html#deployment-on-binder) 
and shown below. 

![Deploying Voila to Binder](./images/publish-binder-notebook-voila.png)


## Voilà!

- Explore more examples at <https://voila-gallery.org/>.
- Create a Voilà badge with a clickable link to your notebook. See the [README.md](./README.md) or [this guide](https://mybinder.readthedocs.io/en/latest/howto/badges.html).
- [Voilà Example](https://mybinder.org/v2/gh/denisecase/datafun-03-discussion/HEAD?urlpath=voila%2Frender%2Flearning.ipynb)

![Voilà Example](./images/published-to-voila.png)