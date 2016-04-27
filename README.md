# TerminalDictionary

Look up words instantly from your command line.

[script origin](http://apple.stackexchange.com/questions/90040/look-up-a-word-in-dictionary-app-in-terminal) Credit goes to Josh Hunt for initially coming up with the script. This
repository has been created as means to improve it.

# System Requirements

MacOSX 10.5 or later (Tested with OS X 10.11.4 El Capitan, Python 2.7)

Not compatible with Python 3.5

# Installation

Install Python version 2.7 from https://www.python.org/downloads/

Install DictionaryServices framework
```
$ pip install 'pyobjc-framework-DictionaryServices==3.1.1'
```

Set permissions and add to path
```
chmod uo+x ./l
export PATH=$PATH:<path to the script 'l'>
```

# Usage

```
l hello
```
