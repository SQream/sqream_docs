# SQream DB documentation

This is the source files for SQream DB documentation.

The public documentation is available at https://docs.sqream.com

## Make changes

Think a document needs to be changed, improved, added? Open an issue or create a pull request.


## Build the docs Locally

To setup and build on Linux:

* Install `gnu make`, `python 3.7` or later, `python3-venv`

create a virtualenv for sphinx (not under the docs tree), e.g.:

```
> python3 -m venv ~/sphinx
```

activate this in the current shell:

```
> . ~/sphinx/bin/activate
```

you should see `(sphinx)` in your prompt (or the dir you used for the venv)

install sphinx + theme:
```
(sphinx) > pip install sphinx
(sphinx) > pip install sphinx-notfound-page
(sphinx) > pip install sphinx-rtd-theme
```

now you can build the docs. You need to active the venv in the current
shell to do the following:

```
> . ~/sphinx/bin/activate
(sphinx) > cd .../sqream_docs
(sphinx) > make html
```

browse to .../sqream_docs/_build/html/index.html
