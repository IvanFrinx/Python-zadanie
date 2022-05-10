import json
import classdata

frinx = 'frinx-uniconfig-topology:configuration'
native = 'Cisco-IOS-XE-native:native'
channel_group = 'Cisco-IOS-XE-ethernet:channel-group'

def load_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data


def extract_data(data):
    objects = list()
    for i, j in data[frinx][native]['interface'].items():
        for k in j:
            attributes = list()
            attributes.append(i+str(k['name']))
            attributes.append(json.dumps(k))
            if 'description' in k.keys():
                attributes.append(k['description'])
            if 'mtu' in k.keys():
                attributes.append(k['mtu'])
            obj = classdata.Interface(*attributes)
            objects.append(obj)
    return objects

def link_ports(objects, port_ids):
    links = dict()
    for obj in objects:
        conf = json.loads(obj.config)
        if channel_group in conf.keys():
            num = conf[channel_group]['number']
            links[obj.name] = port_ids[num]
    return links     