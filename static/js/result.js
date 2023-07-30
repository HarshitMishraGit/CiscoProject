 // Map
 mapboxgl.accessToken =
 "pk.eyJ1IjoiaGFyc2hpdG1pc2hyYSIsImEiOiJja3dia211b3MwMTd5Mm5xdm1yd2o1dmlxIn0.QQokhJ0cV4yV5EVchp1ymg";
var map = new mapboxgl.Map({
 container: "map",
 style: "mapbox://styles/mapbox/streets-v11",
 center: [79, 21], // setting centre to india
 zoom: 3, // zoomed the maped 3x
});

const fetchLocation = async (ip) => {
 try {
   const response = await fetch(`http://ip-api.com/json/${ip}`);
   const data = await response.json();
   if (data.status === "success") {
     const { lat, lon } = data;
     new mapboxgl.Marker().setLngLat([lon, lat]).addTo(map);
   }
 } catch (error) {
   // console.error(`Error fetching location for IP ${ip}:`, error);
 }
};

const fetchAllLocations = async (ipArray) => {
 for (const ip of ipArray) {
   await fetchLocation(ip);
 }
 console.log("Results:", results);
 return results;
};

// Map
var socket = io();
// Function to stop the packet analysis
function stopAnalysis() {
 socket.emit("close");
}

// Function to reconnect to the server
function reconnect() {
 console.log("start clicked");
 socket.connect();
 // Event listener to start receiving timer updates from the server
}
$(document).ready(function () {
 // Function to update the timer on the page
 function updateTimer(timer) {
   $("#timer").text(timer);
 }
 socket.on("connect", function () {
   socket.emit("get_packets");
 });

 // Event listener for receiving timer updates from the server
 socket.on("packets_info", function (packet) {
   timer = packet.timer;
   updateTimer(timer);
   //console.log(obj)
 });

 // Initialize the DataTable
 // var table = $('#packets-table').DataTable();

 socket.on("Completed", function (data) {
   localStorage.setItem("data", JSON.stringify(data));
   console.log("Packets reached =>", data);
   // stopAnalysis();
   $(".loader").addClass("hidden");
   $("#state").text("Analyzed :");
   plotData();
   plotPacketData();
   fetchAllLocations(data.unique_ip);
 });
 const plotPacketData = () => {
  
  
   
   // Prepare the data for the line graph
   var chartData = {
     labels:['Packet Transmission','Packet Retransmission'],
     datasets: [
       {
         label: "Packet Transmission/Retransmission Quantity",
         data:[14987,150],
         backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(255, 159, 64, 0.2)',
         
        ],
        borderColor: [
          'rgb(255, 99, 132)',
          'rgb(255, 159, 64)',
          
        ],
         borderWidth: 1,
        
       },
     ],
   };

 

   // Create the line graph
   var ptx = document.getElementById("packetChart").getContext("2d");
   new Chart(ptx, {
     type: "bar",
     data: chartData,
    //  options: chartOptions,
   });
 };
 const plotData = () => {
   // Extract the protocols from the packets
   let datapackets = JSON.parse(localStorage.getItem("data"));
   var protocols = datapackets.packets.map(function (packet) {
     return packet.protocol;
   });
   // Count the occurrences of each protocol
   var protocolCounts = {};
   protocols.forEach(function (protocol) {
     protocolCounts[protocol] = (protocolCounts[protocol] || 0) + 1;
   });

   // Generate an array of background colors using a color palette
   var colorPalette = [
     "#FF6384",
     "#36A2EB",
     "#FFCE56",
     "#4BC0C0",
     "#9966FF",
     "#FF9F40",
     "#C9CBCF",
     "#67B8E3",
     "#8C9EFF",
     "#FF75A0",
     "#FFEB3B",
     "#3F51B5",
     "#FF5722",
     "#607D8B",
     "#E91E63",
     "#9C27B0",
     "#2196F3",
     "#009688",
     "#FF9800",
     "#795548",
   ];
   var backgroundColors = Object.keys(protocolCounts).map(function (
     protocol,
     index
   ) {
     return colorPalette[index % colorPalette.length];
   });

   // Prepare the data for the pie chart
   var chartData = {
     labels: Object.keys(protocolCounts),
     datasets: [
       {
         data: Object.values(protocolCounts),
         backgroundColor: backgroundColors,
       },
     ],
   };
   // Create the pie chart
   var ctx = document.getElementById("protocolChart").getContext("2d");
   new Chart(ctx, {
     type: "pie",
     data: chartData,
     options: {
       // Customize the chart options
       tooltips: {
         callbacks: {
           label: function (context) {
             let label = context.dataset.label || "";
             console.log(label);
             // Return an empty string to prevent displaying the tooltip
             return "";
           },
         },
       },
     },
     onHover: function (event, elements) {
       if (elements.length) {
         // Retrieve the index of the hovered segment
         const index = elements[0].index;
         // Retrieve the label of the hovered segment
         const label = chart.data.labels[index];
         // Log the label name in the console
         console.log("label => ", label);
       }
     },
   });
    };
    


   
});