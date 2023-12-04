# Experimental-work - Concatenated-index
This repository is used for experimental work for "Infrastruktura za podatke velikog obujma" course on Faculty of informatics and Digital Technologies. It covers bencmarking of read requests response time with and without concatenated index.  The complete Django web app source code and neccessary Docker files are given which are described later.

# Description for using
After downloading the .zip file (and extracting it and opening it in your text editor) from Github or after cloning it in your text editor, open the terminal and move to the root folder that contains extracted files.
```
cd yourPath/rootFolder
```
If you already are in the root folder (where the Dockerfile is located), build your docker image with:
```
docker build -t yourChosenName .
```

and then run the container with:
```
docker run -p 8000:8000 yourChosenName
```
After running the container, the app should be available on URL:
```
http://localhost:8000
```
