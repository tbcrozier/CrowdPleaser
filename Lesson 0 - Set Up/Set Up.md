# Setup
First, let's install the necessary packages.

We'll be using [Python](https://www.python.org) and [Flask](http://flask.pocoo.org/) (in addition to HTML and CSS).

## Python
### Windows
For Windows machines, you'll have to download and install Python3 from [this page](https://www.python.org/downloads/windows/).
TODO: add a screenshot showing the "add python to path" option
### OSX
For Macs, you'll need to install XCode, HomeBrew and then Python3. You'll do all of this from a terminal.

To open a terminal, press Command-Space to open Spotlight Search, then type `terminal` and hit Enter.

![Opening Terminal on OSX](https://github.com/tbcrozier/Ravenwood_My1stCode/wiki_files/open_terminal_osx.gif)

#### XCode
Once you're in the terminal, type `xcode-select --install` and hit Enter.

#### Homebrew
In the terminal, copy and paste this command: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` and hit Enter.

#### Python3
Now you're ready to install Python3:
Type `brew install python3` in the terminal and hit Enter.

## Check Python Installation
Now that you've installed Python3, make sure it works by running python in the terminal.

### Windows
In the Start Menu, type "command". You should see an option for "Command Prompt". Click on that- now you're in the terminal!

Type `python` and press enter.

### OSX
In the terminal from before, type `python` and hit enter.


For both operating systems, you should see something like this:
```
Python 3.5.1 (default, Jan 22 2016, 08:54:32) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Now you can type `exit()` and hit enter to exit Python.

Congratulations, you now have Python set up on your machine!

## Pip
Pip is Python's package management system. We'll use it to install Flask and other packages.

## Installing
For both operating systems, you'll need to download [this script](https://bootstrap.pypa.io/get-pip.py). Move it to your desktop.

In the terminal, you'll need to change your directory (in these examples, `cd` is short for `change directory`)
### Windows
In the terminal, type `cd C:\Users\(username)\Desktop`, replacing `(username)` with your username, and hit Enter.

Now type `python get-pip.py` and hit enter.

### OSX
In the terminal, type `cd ~/Desktop` and hit Enter.

Now type `python get-pip.py` and hit enter.

## Flask
Now you can install Flask!

From the terminal, type `pip install flask` and hit enter.

# Next Steps
You should now have Python and Flask installed. You can follow [this tutorial](https://pythonspot.com/en/flask-web-app-with-python/) to get acquainted with Flask, and we'll go from there!
