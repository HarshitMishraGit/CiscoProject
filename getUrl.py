import pyshark as ps

cap = ps.FileCapture('upload/http_tcp_80_traffic.pcap')
packets = []
error_packets = []
total_length_analyzed = 0
unique_ip = set()
total_seq_number = set()
retransmitted_seq_number = []

for i, packet in enumerate(cap):
    try:
        # packet_info = {
        #     'time': packet.sniff_time.strftime('%d %b %Y %I:%M:%S.%f %p'),
        #     'source': packet.ip.src_host,
        #     'destination': packet.ip.dst_host,
        #     'protocol': packet.highest_layer,
        #     'length': int(packet.length)
        # }
        # total_length_analyzed += int(packet.length)
        # packets.append(packet_info)
        # unique_ip.add(packet.ip.src_host)
        # unique_ip.add(packet.ip.dst_host)
        if 'tcp' in packet:
            if packet.tcp.seq in total_seq_number:
                retransmitted_seq_number.append(packet.tcp.seq)
            else:
                total_seq_number.add(packet.tcp.seq)

    except Exception as e:
        pass
print(f'Retransmitted Packets :{retransmitted_seq_number}')
