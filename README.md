# PDF invoice for Small and Medium Businesses
This is a quick guide to getting started with the codebase for invoice. 

## Pre-requirements
The system should have Python 3.x and pip installed for Python 3.x

For Windows, get help here:
https://phoenixnap.com/kb/how-to-install-python-3-windows
https://www.onlinetutorialspoint.com/mysql/install-mysql-on-windows-10-step-by-step.html

## Getting Started with the codebase
Pull the codebase into your system.
Make sure your directory is python executable.



As a good practice, it is advisible to work under a virtual environment for every python project.
You can install virtualenv using 
`sudo apt install virtualenv` for ubuntu
`pip install virtualenv` for windows
or if your system follows `pip3`use:
`pip3 install virtualenv`

Once you create the virtual environment, activate it using the command: 
`source env/bin/activate` for ubuntu/mac
`source env\Scripts\activate.bat`

For more information on installing and activating virtual env you can checkout(VirtualEnvWrapper-win is not needed): https://www.liquidweb.com/kb/how-to-setup-a-python-virtual-environment-on-windows-10/

## Installing Essentials
`requirements.txt` file contains all the needed libraries. You can simply pip install them from the directory containing the requirements file. I would highly recommend to use virtual env before doing any pip install
```
pip install -r requirements.txt
```
or if your system follows `pip3`use:
```
pip install -r requirements.txt
```
## Follow the guide next
Once your dependencies are installed. Look over the directory(folder) and you'll get a folder named `assets`. Put you logo inside this folder.

## Running the program
Run the python file: 
```
python generate_invoice.py
```
It will then ask for all the user information related to the invoice. The program will then create the invoice inside a folder named `output`(which will be created if not present) within this directory. 


That's it. The program will then process the files. 

Checkout out other content on TheCodeWork (https://thecodework.com)
## 🎉 Happy Invoicing. 🎉
