# CiscoProject
This is the visualization of TCP/HTTPS packets
transmittion and reception in Pyhton with the functionality of wireshark 
with the python package "Pyshark"

# Data Files
You can get all the .pcap file for testing here

➡️ https://drive.google.com/drive/folders/1EczYcR_yyGM2ON6a39t5XMw_2ECdreyr?usp=sharing

Here we need to user sockets to continuously analyzing the packets in the frontend.
For that we need to install flask-socket
```dtd
pip install flask-socketIO
```
    

* First try to emit and receive a simple timer to check the connection and working on sockets.
It basically trigger on event and Pull/Push data from Server to Client or vice versa and make
it very easy to see the progress or the analyzed packet at any point of time
* For this you have to include the cdn of socket.io in your html file
  * ```dtd
     <script src="https://cdn.socket.io/4.6.0/socket.io.min.js" integrity="sha384-c79GN5VsunZvi+Q/WObgk2in0CbZsHnjEqvFxC5DxHn9lTfNce2WW6h2pH6u/kF+" crossorigin="anonymous"></script>
  * Now check the code at commit https://github.com/HarshitMishraGit/CiscoProject/tree/d050480158534f4f3d7a4227ac72b432cce31a1e
  * This will easily give some introduction to the socket in web 
    * check  -> main.py 
    * template -> test.html
