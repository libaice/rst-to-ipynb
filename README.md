# rst-to-ipynb

This project converts between a standalone
[reStructuredText](http://docutils.sourceforge.net/rst.html) file
and a [IPython Notebook](http://ipython.org/notebook.html) file.

This is currently achieved by converting to markdown with
[pandoc](http://pandoc.org) and then to IPython notebook using
[notedown](https://github.com/aaren/notedown/), plus some
configuration and tweaks.

## Usage

To produce xxx.ipynb from xxx.rst:

   python convert.py xxx.rst -o xxx.ipynb

## Example

- [all.rst]()
- [all.ipynb](http://nbviewer.ipython.org/github/nthiery/rst-to-ipynb/blob/master/tests/all.ipynb)

## TODO:

- [X] Handle Sage's doctests
- [X] Fenced code blocks: fix incompatibility between pandoc output and notedown input.  
      Fixed in notedown; see: https://github.com/aaren/notedown/issues/29.
- [ ] Configurability of the default ReST role, in particular to handle maths in Sage's ReST dialect.
      Current status: hardcoded for Sage.
- [ ] Configurability of custom ReST roles, in particular to handle Sage's custom roles
- [ ] Proper argument parsing; escape characters, spaces, ... are not
      yet supported
- [ ] Handle input/output blocks within itemize and other indented constructions  
      See https://github.com/aaren/notedown/issues/33
