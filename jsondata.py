import json
import classdata


def load_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data


frinx = 'frinx-uniconfig-topology:configuration'
interfaces = "openconfig-interfaces:interfaces"


def extract_data():
    data = load_json('configClear_v2.json')
    objects = list()
    for i in data[frinx][interfaces]['interface']:
        if 'Loopback' not in i['name']:
            if 'description' not in i['config'].keys():
                i['config']['description'] = None
            if 'mtu' not in i['config'].keys():
                mtu = None
            else:
                mtu = int(i['config']['mtu'])
            interface = classdata.Interface(i["name"], json.dumps(i["config"]),
                                            i['config']['description'], mtu)
            objects.append(interface)
    return objects

        # for i in data[frinx]['Cisco-IOS-XE-native:native']['interface']:
        #     for i in data[frinx]['Cisco-IOS-XE-native:native']['interface'][i]:
        #         if 'Cisco-IOS-XE-ethernet:channel-group' in i.keys():
        #             print(i['Cisco-IOS-XE-ethernet:channel-group'])
