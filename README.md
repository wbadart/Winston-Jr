# Winston-Jr
#### The next generation of Winston.

Fully revamped and translated from Ruby to Python, Winston Jr. promises to live up to and even surpass his father's legacy.  Jr. features more flexible input recognition, a refactored error function, and new sentence generation algorithms.  While still a work in progress, Jr. grows every day, developing more advanced code and reading more articles!

As always, stay tuned for updates!

##### Current functions:
Name | Description
-----|------------
add  | Manually add a single sentence or text file containing sentences to the database.
edit | Alter the data associated with the word, i.e. its name and position array.
error| Displays possible errors, keeps log. Displays log with -l flag.
find | Look up a word and its associated data.
help | Prints availible commands and options.
list | Lists words in selected dictionary.
new  | Synthesizes a sentence - this function is the end goal of the program.
sort | Alphabetizes dictionary.

The program contains other, less important functions as well. To view the details of these functions and the functions listed above, please run `main.py` and use `help`.

- - - -

### Getting Started with Winston

Starting your own instance of Winston Jr. is very simple.  You have a couple options.

#### 1. Cloning the repository

  From the main repo screen, simply click "clone in desktop" and follow the prompts. You can find and run `main.py` from the directory you specified during cloning.

#### 2. Downloading the zip

  Near the "clone" button is a "download as zip" button. Click this. Now extract the zip file, and run `main.py`.

#### 3. Bower install

  Winston Jr. is not a Bower-registered repository, but you can still use Bower to install. Once you know that Bower is part of your path (which it should be if you did a global install with NPM), simply enter the command `bower install wbadart/Winston-Jr`.
