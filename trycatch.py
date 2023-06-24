import pyshark as ps
import time
start = time.time()
cap=ps.FileCapture('data/http_tcp_80_traffic.pcap')
i=1
for packet in cap:
    # print(dir(packet))
    print(packet)
    break
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
print(end - start)