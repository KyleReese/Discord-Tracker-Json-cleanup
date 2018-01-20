import ijson
import ftfy
json_data=open("dht.txt", "rb")
file = open('dhtfixed.txt','wb')
channelId = '84764735832068096'
objects = ijson.items(json_data, 'data.' + channelId)

for thing in objects:
	for item in thing:
		line = ftfy.fix_text(thing[item]['m'])
		try:
		    file.write(line.encode("utf-8"))
		except:
		    print("err: ",repr(line))
		    break
		file.write('\n'.encode("utf-8"))
