# Small REST API for Python 3

This repository contains code that is created for REST APIs with Flask and Python.

**Requirements**: Python 3.5.3+, Flask, Postman

# Quickstart

Install Flask using `pip3`:
```bash
$ pip3 install Flask
```

Install flask-admin using `pip3`:
```
pip3 install flask-admin
```

Install last version of Postman(will be used as admin panel and test): 
https://www.getpostman.com/apps

Import requests for Postman:

  * open Import as it shows on the pic
  <p align="center">
    <img src="https://github.com/frozmannik/REST_API/blob/master/Screenshot%20from%202018-03-07%2015-39-55.png" >
  </p>
 *  Copy following link: https://www.getpostman.com/collections/90294222199bc6358318 into 'Import From Link'
  
<p align="center">
    <img src="https://github.com/frozmannik/REST_API/blob/master/Screenshot%20from%202018-03-07%2015-43-18.png" >
  </p>
  
  * Press Import
  
  <p align="center">
    <img src="https://github.com/frozmannik/REST_API/blob/master/Screenshot%20from%202018-03-07%2015-43-30.png" >
  </p>
  
  * Now we can see list of requests
 
 <p align="center">
    <img src="https://github.com/frozmannik/REST_API/blob/master/Screenshot%20from%202018-03-07%2015-50-13.png" >
  </p>
  
 
# Requests description:
* 
    <img src="https://github.com/frozmannik/REST_API/blob/master/pics/Screenshot%20from%202018-03-07%2016-03-11.png" > shows a list of all items
  
* 
    <img src="https://github.com/frozmannik/REST_API/blob/master/pics/Screenshot%20from%202018-03-07%2016-03-21.png" >  shows a description of specific title
  
* 
    <img src="https://github.com/frozmannik/REST_API/blob/master/pics/Screenshot%20from%202018-03-07%2016-03-28.png" > add new title if such title doesn't exist, if it exists shows an error. Requires a JSON file to proceed
  
* 
    <img src="https://github.com/frozmannik/REST_API/blob/master/pics/Screenshot%20from%202018-03-07%2016-03-35.png" > add new title if such title doesn't exist, if it exist modify it. Requires a JSON file to proceed
  
* 
    <img src="https://github.com/frozmannik/REST_API/blob/master/pics/Screenshot%20from%202018-03-07%2016-03-41.png" > delete title if such title exist
  
# Run the application:
Open a terminal in project folder
```
$ python __main__.py 
 Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Open a Postman: </p>
* Selecet needed request and press <i>send</i> </p>
<img src="https://github.com/frozmannik/REST_API/blob/master/pics/Screenshot%20from%202018-03-07%2016-26-35.png" >

* If request(POST and PUT) requires a JSON enter it in <i>Body</i> menu how it shows and press <i>Send</i> <img src="https://github.com/frozmannik/REST_API/blob/master/pics/Screenshot%20from%202018-03-07%2016-34-03.png" >


