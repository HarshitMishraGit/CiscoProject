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
    * Now check the code at
      commit https://github.com/HarshitMishraGit/CiscoProject/tree/d050480158534f4f3d7a4227ac72b432cce31a1e
    * This will easily give some introduction to the socket in web
        * check -> main.py
        * template -> test.html
* To show the progress of analyzing the packet , we should know the total number
  of packets we are analyzing and for that first you should read the .pcap dump file by wireshark
  and then use it
    *     pip install pyshark 
    * This is a python wrapper for the command line tool of wireshark named : tshark(command line tool of wireshark)
    * This is having diffrent mode of analyzing like-
        * FileCapture
        * LiveCapture
    * we are using FileCapture which will analyze the wireshark dumpFile
        *   ```dtd
            cap = ps.FileCapture('upload/http_tcp_80_traffic.pcap')
            cap.load_packets()
            total_packet_length = len(cap)
    * Iterate over the packets
        *   ```dtd 
            for i, packet in enumerate(cap):
            progress = int((i + 1) / total_packet_length * 100)

# Showing Chart using chart.js

Now chart.js is a very powerful javascript library to plot almost all
type of chart .We use it to display diffrent data related to packet Analyzation.

1. First You should include the library in the template (result.html)
   ```dtd
     <script src="https://cdn.jsdelivr.net/npm/chart.js@3.5.1/dist/chart.min.js"></script>
    ``` 
2. Create a canva with a specific ID to initialize the chart
   ```dtd
     <canvas id="protocolChart"></canvas>
    ```
3. Fill the data from backend to plot the chart
    * So here we will give the data just after completion of analyzing and then it will
      plot a pi-chart (circular shap chart) to show diffrent type of protocol used in the packets
    * ```dtd
      var ctx = document.getElementById("protocolChart").getContext("2d");
      new Chart(ctx, { 
            type: "pie",
            data: chartData,
            options: {
                // give any options if required
               }
      )
      ```
4. And that's it , You are good to go
   ![img.png](img.png)

## Result

You will get all the protocols involved in all the packets and the ip locations on the map.
![img_1.png](img_1.png)
![img_2.png](img_2.png)
