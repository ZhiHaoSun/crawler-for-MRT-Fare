#!/usr/bin/python
#coding:utf-8

from FilmURLSpider import SpiderDytt8
import json
import os

content = ""
with open('mrt_code.json', 'r') as content_file:
    content = content_file.read()
mrt_codes = json.loads(content)
length = len(mrt_codes)

dytt8spider = SpiderDytt8()

for i in range(13,length):
	start = mrt_codes[i]
	start_id = start["id"]
	start_name = start["name"]
	print start_name
	fares = []

	for j in range(0,length):
		end = mrt_codes[j]
		end_id = end["id"]
		end_name = end["name"]
		url = "https://www.mytransport.sg/content/mytransport/home/commuting/busservices/jcr:content/par/mtp_generic_tab/mtp_generic_tab6/distancefare.mrtFare?entryMarkerId=" + start_id +"&exitMarkerId=" + end_id + "&ticketType=30"
		content = dytt8spider.openUrl(url)
		fare = dytt8spider.getFare(content)
		fare_dict = {}
		fare_dict["name"] = end_name
		fare_dict["dis"] = fare[0].get_text()
		fare_dict["fare"] = fare[1].get_text()
		fares.append(fare_dict)
		print "name  " + end_name + "  ,  " + "dis  " + fare_dict["dis"] + "  ,fare   " + fare_dict["fare"]
	result = {}
	result[start_name] = fares
	filename = str(i) + "_" + start_name + "_fare.json"

	write_json = open(filename , 'w+')
	write_json.write(json.dumps(result))
