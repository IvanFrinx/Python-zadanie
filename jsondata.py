import json
import classdata

frinx = 'frinx-uniconfig-topology:configuration'
native = 'Cisco-IOS-XE-native:native'
channel_group = "Cisco-IOS-XE-ethernet:channel-group"

def load_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data


def extract_data(data):
    objects = list()
    for i in data[frinx][native]['interface'].keys():
        for j in data[frinx][native]['interface'][i]:
            if 'description' not in j.keys():
                j['description'] = None
            if 'mtu' not in j.keys():
                j['mtu'] = None   
            obj = classdata.Interface(i+str(j['name']), j["description"], json.dumps(j), j['mtu'])
            objects.append(obj)
    return objects

def link_ports(objects, port_ids):
    links = dict()
    for obj in objects:
        conf = json.loads(obj.config)
        if channel_group in conf.keys():
            num = conf[channel_group]['number']
            if num in port_ids.keys():
                links[obj.name] = port_ids[num]           
    return links     