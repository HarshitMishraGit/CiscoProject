import pyshark as ps
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HarshitMishra123'  # Replace with your own secret key
socketio = SocketIO(app)
cap = ps.FileCapture('upload/http_tcp_80_traffic.pcap')
packets = []
error_packets = []
total_length_analyzed = 0
unique_ip = set()


@app.route('/', methods=['GET', 'POST'])
def index():
    global cap, packets, error_packets, total_length_analyzed
    # cap = ps.FileCapture('upload/http_tcp_80_traffic.pcap')
    # print(cap)
    if request.method == 'POST':
        file = request.files['file']
        file.save('upload/http_tcp_80_traffic.pcap')
    # return render_template('result.html', packets=packets, error_packets=error_packets, total_length=total_length_analyzed)
    return render_template('result.html')


@socketio.on('connect')
def handle_connect():
    @socketio.on('get_packets')
    def get_packets():
        global cap, packets, error_packets, total_length_analyzed
        # Emit the initial data to the client
        # socketio.emit('packets_info', {
        #     'packets': packets,
        #     'error_packets': error_packets,
        #     'total_length': total_length_analyzed
        # })
        timer = 1
        for packet in cap:
            try:
                packet_info = {
                    'time': packet.sniff_time.strftime('%d %b %Y %I:%M:%S %p'),
                    'source': packet.ip.src_host,
                    'destination': packet.ip.dst_host,
                    'protocol': packet.highest_layer,
                    'length': int(packet.length),
                }
                total_length_analyzed += int(packet.length)
                packets.append(packet_info)
                unique_ip.add(packet.ip.src_host)
                unique_ip.add(packet.ip.dst_host)
                # socketio.emit('packets_info', {
                #     'packets': packets,
                #     'error_packets': error_packets,
                #     'total_length': total_length_analyzed
                # })
                # socketio.sleep(10)
                # print(packet_info)
                socketio.emit('packets_info', {
                    'timer': timer
                })
                # socketio.sleep(1)  # Wait for 1 second
                timer += 1
            except Exception as e:
                error_packets.append(packet)
                # print(f"Error analyzing packet: {e}")
        socketio.emit('Completed', {
            'packets': packets,
            'total_length': total_length_analyzed,
            'unique_ip': list(unique_ip)
        })


if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app, allow_unsafe_werkzeug=True)
