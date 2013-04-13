ceylon-sublimetext
==================

Simple Ceylon Sublime Text 2 package.

It proposes:
- colour highlighting,
- some snippets,
- a build system.

Syntax highlighting
-------------------

The syntax highlighting should be compatible with Text Mate.


Build
-----

The build system searches the module name of the file that need to be compiled by traversing the parent directories (including the directory containing the file) for a 'module.ceylon' file. 

If the ceylon command isn't in your PATH, you'll need to complete 'Ceylon.sublime-build' and 'CeylonModule.sublime-build' to set the command right.

Note: On MacOS X, Sublime Text doesn't seem to load '.bash_profile'.
