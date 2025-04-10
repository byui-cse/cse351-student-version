# Software Used in the Course

## Python 3

We will be using Python throughout the course. Please ensure that you have version 3.13.x or higher; it is preferred to have the latest version of Python. Python can be [downloaded here](https://www.python.org/downloads/).
 

## Python Videos

If any of the concepts or topics in the list below seem unfamiliar to you, you should review them. The following are MicroSoft videos.

- [Introducing Python](https://www.youtube.com/watch?v=7XOhibxgBlQ&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=2)
- [Getting Started](https://www.youtube.com/watch?v=CXZYvNRIAKM&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=3)
- [Configuring VS Code](https://www.youtube.com/watch?v=EU8eayHWoZg&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=4)
- [Input and print functions](https://www.youtube.com/watch?v=FhoASwgvZHk&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=5)
- [Demo of print function](https://www.youtube.com/watch?v=FhoASwgvZHk&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=6)
- [Comments](https://www.youtube.com/watch?v=kEuVvUc1Zec&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=7)
- [String data type](https://www.youtube.com/watch?v=FhoASwgvZHk&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=9)
- [Numeric data types](https://www.youtube.com/watch?v=FhoASwgvZHk&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=13)
- [Date data types](https://www.youtube.com/watch?v=o1dlxoHxdHU&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=15)
- [Collections](https://www.youtube.com/watch?v=beA8IsY3mQs&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=25)
- [Loops](https://www.youtube.com/watch?v=LrOAl8vUFHY&[list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=27)
- [Python dictionaries: realpython](https://realpython.com/lessons/dictionary-python/)
- [Python slicing](https://www.youtube.com/watch?v=ajrtAuDg3yw)

## Links to Python Articles

- [Python.org](https://www.python.org/)
- [Python lists](https://www.w3schools.com/python/python_lists.asp)
and [Lists and Tuples in Python](https://realpython.com/courses/lists-tuples-python/)
- [Python Dictionaries: w3 school](https://www.w3schools.com/python/python_dictionaries.asp) 
- [Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)
- [To learn more about installing modules using the **pip** command](https://docs.python.org/3/installing/index.html#basic-usage)
 

## Visual Studio Code (vscode)

There are a number of code editors available to programmers. You are free to use any editor that you want. However, the course will use Visual Studio Code as the editor in video examples and during class time. VSCode can be downloaded at [VSCode](https://code.visualstudio.com)

## Python Package in VSCode 

When you open a Python file, VSCode will want you to install the Python Package from MicroSoft. Please install it.

![](assets/code-python-package.png)

## You Will Install Python Packages for this Course

The course uses the several Python packages that must be installed on your computer, they are listed in the next section. Keep in mind that a computer can have more than one version of Python. It is important that these packages are installed on the version of Python that is used in VSCode and required for this class; at least 3.10 but the latest version preferably.

1. Open VSCode and create a Python file that will print out `Hello World`

```python
print('Hello World')
```

2. Run the program and notice the output in the terminal window. **Reminder**: You can't run a Python file until you save it on your computer. The terminal window displays the full path of Python in yellow (ie., `"C:/users/.../python.exe"`) in the image below; you may not have it displayed in yellow on your computer. **Your path will most likely be different than what is pictured here**:


![](assets/running-python.png)


3. Select and copy the full Python path and paste it in that terminal window. Include any quotes that might be around this path. In most cases for Mac users, the python path will just be `python3`. You will have quotes if the path has spaces in it. Then add the options `-m pip install <package>` where `<package>` is the name of the package you want to install. For example: In the case of numpy, it would be:

```
<python path used in VS Code> -m pip install numpy
```

Note that Mac users might need to add `--user` to the install command line. Also, Mac users can try `pip3 install --user <package>` in the terminal app to see if that works on their computer.


## Packages that are installed with Python

We will be using the following packages that are already installed on you computers.

- **threading**: Threading package that allows for the creation and management of threads
- **multiprocessor**: Process package that allows for the creation and management of processes


## CSE351 Library

To simplify the process of creating your assignments we have created a Python package that contains common libraries (additional packages) we expect you to use. Please follow this link for more information about the [CSE 351 Course Package](package.md)