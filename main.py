import pyshark as ps
import pandas as pd
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
    print(packet.frame_info.)
    # print(packet.eth.dst)
    # print(packet.eth.src)
    # print(packet.eth._all_fields)
    # print(packet.eth.type)
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





