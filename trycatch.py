import pyshark as ps
import time
import os
from dotenv import load_dotenv

load_dotenv()
start = time.time()
cap = ps.FileCapture('upload/http_tcp_80_traffic.pcap', use_ek=True)
# total_packets = len([packet for packet in cap])
packets = []
i = 1
print("MAPBOX API", os.getenv("MAPBOX_API"))
exit()
# print(len([packet for packet in cap]))
cap.load_packets()
# packet_amount = len(cap)
# print(packet_amount)
# exit()

for i, packet in enumerate(cap):
    # print(dir(packet))
    if 'ip' in packet:
        print("Source => ", packet.ip.src_host)
        print("Destinatio =>", packet.ip.dst_host)
    # packets.append(packet)
    # Calculate progress percentage
    # progress = int((i + 1) / total_packets * 100)
    # print("progress=> ",progress)
    # print(packet.tcp.options)
    # print(packet.tcp.field_names)
    # print(packet.tcp.option_len)
    # print(packet.tcp.field_names)
    # try:
    #     if packet.has_field('ipv6'):
    #         ipv6 = packet.ipv6
    #         print(ipv6.src_host, "  -> version =>  ", ipv6.version)
    #     elif packet.has_field('ip'):
    #         ip = packet.ip
    #         print(ip.src_host, "  -> version =>  ", ip.version)
    #     print('i => ', i)
    #     i += 1
    #     if i == 10:
    #         break
    # except Exception as e:
    #     print("Exception:", str(e))
    #     continue

end = time.time()
print("Time in Analyzation => ", end - start)
