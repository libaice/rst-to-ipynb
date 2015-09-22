
# rst-to-ipynb
This project converts between a standalone
[reStructuredText](http://docutils.sourceforge.net/rst.html) file
and a [IPython Notebook](http://ipython.org/notebook.html) file.

## Example
`python convert.py tests/test.rst tests/test.ipynb` produces [test.ipynb] from
[test.rst].

[test.rst]:https://github.com/scottsievert/rst-to-ipynb/blob/master/tests/test.rst
[test.ipynb]:http://nbviewer.ipython.org/github/scottsievert/rst-to-ipynb/blob/master/tests/test.ipynb

## TODO:

- [ ] Configurability of the default ReST role, in particular to handle maths in Sage's ReST dialect
- [ ] Properly parse args passing in; spaces/etc (anything with escape
      characters) are not supported

- [X] Handle Sage's doctests
- [X] Fenced code blocks: fix incompatibility between pandoc output and notedown input

  Fixed in notedown; see: https://github.com/aaren/notedown/issues/29.
