# GoogleIt
Surfing the web in the easiest way with python.

# Introduction
In this program , I tried to create an environment where you can find the weblinks for a subject from google.

This program is easy to install and easy to use, and it has the ability of safe search, where our firewall will block the websites that are unsafe.

# Commands
Our main file is index, so you can run the program with :
```shell
python3 index.py
```
Default query is "google", so for setting the query you want use "-q" like this :
```shell
python3 index.py -q "java script"
```
You can set the output file name , if you don't it will set it as the query :
```shell
python3 index.py -q "java" -o "myresult"
```
For having a safe search and using firewall , just add "-s" to your command :
```shell
python3 index.py -q "maven" -s
```
Each web searching for safe search has a timeout, you can set the timeout like this :
```shell
python3 index.py -q "xml" -s -t 5
```

# Final words
In this program , my target was to surf the web in a safe way, and save the links that I want.

Contact me at : najafizadeh21@gmail.com of officialamirhossein21@gmail.com
