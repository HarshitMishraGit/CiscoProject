import pyshark as ps
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import asyncio

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


async def get_length():
    global cap
    await cap.load_packets()
    return len(cap)


@socketio.on('connect')
def handle_connect():
    # total_length_packet=get_length()
    @socketio.on('get_packets')
    def get_packets():
        global cap, packets, error_packets, total_length_analyzed
        timer = 1
        for i, packet in enumerate(cap):
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
                    'timer': i + 1,

                })
                # socketio.sleep(1)  # Wait for 1 second
            except Exception as e:
                error_packets.append(packet)
                socketio.emit('packets_info', {
                    'timer': i + 1,
                })
                # print(f"Error analyzing packet: {e}")
        socketio.emit('Completed', {
            'packets': packets,
            'total_length': total_length_analyzed,
            'unique_ip': list(unique_ip)
        })

    @socketio.on('close')
    def handle_close():
        socketio.emit('closed', {
            'message': "connection is closed ."
        })
        socketio.stop()


if __name__ == '__main__':
    app.run(debug=True)
    socketio.run(app, allow_unsafe_werkzeug=True)
