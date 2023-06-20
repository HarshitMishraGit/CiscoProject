import pyshark as ps
import pandas as pd
import xmltodict
import datetime
import json
# from flask import Flask, render_template, request
# app = Flask(__name__)
cap=ps.FileCapture('httpCapture.pcap')
packets = []
for packet in cap:
    # Extract relevant information from the packet
    # packet_info = {
    #     'time': packet.sniff_time,
    #     'source': packet.eth.src,
    #     'destination': packet.eth.dst,
    #     # 'protocol': packet.highest_layer,
    #     # 'data': packet.data.data if hasattr(packet, 'data') else None,
    #     # Add more fields as per your requirements
    # }
    # packets.append(packet_info)
    # print(packet.frame_info)
    # print(packet.get_multiple_layers)
    # print(packet.get_raw_packet)
    # print(type(packet.ipv6))
    # print(packet.layers)
    # my_dict = xmltodict.parse(packet.ipv6)
    # print(my_dict)
    # print(packet.eth.dst)
    # print(packet.eth.src)
    # print(packet.eth._all_fields)
    # print(packet.eth.type)
    print(dir(packet))
    # print(packet.length)
    # print(dir(packet.tcp))
    # print(dir(packet.eth.src_ig))
    # print(packet.eth.src)
    # print(packet.eth.dst)
    # print(packet.eth.type)
    # print(packet.eth.src_resolved)
    # print(packet.eth.dst_oui_resolved)
    # print(packet.frame_info)
    # print(packet.frame_info.protocols.split(':'))
    # print(packet.frame_info.cap_len)
    # print(packet.frame_info.time_epoch)
    # time_string = datetime.datetime.fromtimestamp(float(packet.frame_info.time_epoch)).strftime('%Y-%m-%d %H:%M:%S')
    # print(time_string)
    # print(packet.frame_info.cap_len)
    # print(dir(packet.ipv6))
    # print(packet.ipv6.field_names)
    # print(packet.ipv6.version)
    # print(packet.ipv6.ip_version)
    # print(packet.ipv6.tclass)
    # print(packet.ipv6.tclass_dscp)
    # print(packet.ipv6.src_host)
    # print(packet.ipv6.dst_host)
    # print(packet.ipv6.hlim)
    # print(dir(packet.layers))
    # print(packet.layers)
    print(packet.tcp.field_names)

    break
    # fp=open("properties.txt","w")
    # pacProp=dir(packet)
    # for prop in pacProp:
    #     if '__' in prop:
    #         continue
    #     fp.write(f"----------------------------------[ {prop} ]---------------------------------------------\n")
    #     propProp=dir(prop)
    #     if propProp :
    #         for propProperties in propProp:
    #             fp.write(propProperties+'\n')
    #     fp.write("==========================================================================================\n\n")
    # fp.close()
    # break






# create a dataframe
# df = pd.DataFrame(packets)
# df.to_excel('packet_info.xlsx', index=False)
# print(packets)





