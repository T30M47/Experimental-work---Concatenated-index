# Experimental-work - Concatenated-index
---
This repository is used for experimental work for "Infrastruktura za podatke velikog obujma" course on Faculty of informatics and Digital Technologies. It covers bencmarking of read requests response time with and without concatenated index.  The complete Django web app source code and neccessary Docker files are given which are described later.

# Description for using
---
After downloading the .zip file (and extracting it and opening it in your text editor) from Github or after cloning it in your text editor, open the terminal and move to the root folder that contains extracted files.
```
cd yourPath/rootFolder
```
If you already are in the root folder (where the Dockerfile is located), build your docker image with:
```
docker build -t yourchosenname .
```

and then run the container with:
```
docker run -p 8000:8000 yourchosenname
```
After running the container, the app should be available on URL:
```
http://localhost:8000
```
The home page contains more description on how to benchmark this model, but you can also find some instructions over here:
 1. I used ab (Apache Benchmark) for testing read response time, so You have to install it:
    ### Debian based Linux
    ```
    sudo apt-get install apache2-utils
    ```
    ### Arch based Linux
    ```
    sudo pacman -S apache-tools or just sudo pacman -S apache
    ```
 2. After running the Docker Container with the web app you can use ab to send read requests to specific urls, and i used it like this:
    ```
    ab -n 1000 -c 3 "URL"
    # to send 1000 requests with 3 concurrent requests
    ```
 3. You have four options for URLs based on different types of indexes on different tables with the same types and amount of data:
    *  "http://127.0.0.1:8000/withoutIndex/?naziv=value1&cijena=value2&datum_kreiranja=value3"
    *  "http://127.0.0.1:8000/withIndex/?naziv=value1&cijena=value2&datum_kreiranja=value3"
    *  "http://127.0.0.1:8000/withPartIndex/?naziv=value1&cijena=value2&datum_kreiranja=value3"
    *  "http://127.0.0.1:8000/withWrongIndex/?naziv=value1&cijena=value2&datum_kreiranja=value3"
 4. Here are some combinations that you can put for values in URLs:
    1. for URL without index:
       * first combination: "http://127.0.0.1:8000/withoutIndex/?naziv=improve&cijena=34.21&datum_kreiranja=1989-04-03"
       * second combination: "http://127.0.0.1:8000/withoutIndex/?naziv=gas&cijena=433.57&datum_kreiranja=2015-11-02"
       * third combination: "http://127.0.0.1:8000/withoutIndex/?naziv=beyond&cijena=903.39&datum_kreiranja=1983-04-08"
 5. You can use your own combination if You go to "http://localhost:8000/admin" and login with admin for username and admin for password where you can find specific data and then query it.
