#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()

index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(index, page_size)
count = 0
for key, item in res.items():
    print(key, item)
    if count == 5:
        break
    count += 1
