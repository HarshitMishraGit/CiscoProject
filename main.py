# import pyshark as ps
# import pandas as pd
# import xmltodict
# import datetime
# import json
# from flask import Flask, render_template, request
# app = Flask(__name__)
# # cap=ps.FileCapture('data/http_tcp_80_traffic.pcap')
# packets = []
# error_packet=[]
# total_length_analyzed=0
# # i=0
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         file = request.files['file']
#         file.save('upload/http_tcp_80_traffic.pcap')
#         return render_template('result.html')
#     return render_template('index.html')
#
# @app.route('/result')
# def result():
#     cap = ps.FileCapture('upload/http_tcp_80_traffic.pcap')
#     packets = []
#     error_packets = []
#     total_length_analyzed = 0
#     for packet in cap:
#         # Extract relevant information from the packet
#         try:
#             packet_info = {
#                 'time': packet.sniff_time,
#                 'source': packet.ip.src_host,
#                 'destination': packet.ip.dst_host,
#                 'protocol': packet.highest_layer,
#                 # 'data': packet.data.data if hasattr(packet, 'data') else None,
#                 'Length( in bytes)': int(packet.length),
#                 # Add more fields as per your requirements
#             }
#             total_length_analyzed+=int(packet.length)
#             packets.append(packet_info)
#         except:
#             # print("some error happend ",packet)
#             error_packet.append(packet)
#         # print(packet.frame_info.protocols.split(':'))
#     return render_template('result.html', packets=packets, error_packets=error_packets,total_length=total_length_analyzed)
#     print("Successfully Analyzed - ",len(packets))
#     print("Failed to Analyze - ",len(error_packet))
#     print("Total size of Analyzed data - ", total_length_analyzed)
#
# # create a dataframe
# # df = pd.DataFrame(packets)
# # df.to_excel('packet_info.xlsx', index=False)
# # print(packets)
# if __name__ == '__main__':
#     app.run(debug=True)
import time

import pyshark as ps
from flask import Flask, render_template, request,jsonify
from flask_socketio import SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'HarshitMishra123'  # Replace with your own secret key
socketio = SocketIO(app)
cap = None
packets = []
error_packets = []
total_length_analyzed = 0

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     global cap, packets, error_packets, total_length_analyzed
#
#     if request.method == 'POST':
#         file = request.files['file']
#         file.save('upload/http_tcp_80_traffic.pcap')
#         cap = ps.FileCapture('upload/http_tcp_80_traffic.pcap')
#         for packet in cap:
#             try:
#                 packet_info = {
#                     'time': packet.sniff_time,
#                     'source': packet.ip.src_host,
#                     'destination': packet.ip.dst_host,
#                     'protocol': packet.highest_layer,
#                     'length': int(packet.length),
#                 }
#                 total_length_analyzed += int(packet.length)
#                 packets.append(packet_info)
#             except Exception as e:
#                 error_packets.append(packet)
#                 print(f"Error analyzing packet: {e}")
#         return render_template('result.html', packets=[], error_packets=[], total_length=10)
#
#     return render_template('index.html')

# timer =0

@app.route('/')
def index():
    return render_template('test.html')
@socketio.on('connect')
def handle_connect():
    @socketio.on('get_timer')
    def get_timer():
        timer = 1
        while True:
            socketio.emit('timer_update', timer)
            socketio.sleep(1)  # Wait for 1 second
            timer += 1
# todo: do this
if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app,allow_unsafe_werkzeug=True)

