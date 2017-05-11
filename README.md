# Json_parser

Description:
The task we to design a REST service capable towards parsing a JSON file received from the command line and outputting a list of all palindrome values seen in the file. All APIs were written with Python and the Flask web framework was used in order to design the web application. The loopback address is used to host the web application. The two exposed nodes that a user access use are GET:/palindromes and GET:/palindromes/count.  

The system was the wrapped into a docker container - which could be initialised through use of the docker file that is also availible in the source code. 

- Tips for system use:

To build the docker image- use the command: 
'sudo docker build -t <repo_name> .' 

When running the docker file, use the command:
'sudo docker run -it -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/user/.Xauthority --net=host ekram /bin/bash'

This will load a interactive shell from which you will also be able to run the firefox browser
through the command 'firefox'. Note that we can use the native host's browser in order to run
the web application since both the host and container have the same loop back address.

Due to issues that have occured when trying to recursively copy sub directories, the proposed
solution is to instead copy a zip archive file of the system to the /usr/local/Deeplearni_ng directory
and the have the user unzip the file to test. Note that the zip feature has ben enabled in the container.

The web application will located at the system's loopback address. Open an instance of firefox and type 
the loopback address and port number into the address bar in order to get access to the application. If 
successful, a welcome message should appear. 

To execute source code, go into the src directory and use the following command:
'python ./main.py ../json_object/<input file>'
