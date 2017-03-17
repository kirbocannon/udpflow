from string import Template
import csv

ffan_file = 'flowfan.xml'
csv_file = 'hosts.csv'



xml_open ='''<?xml version="1.0" encoding="UTF-8"?>
<flowfan>
<flowfan>'''

xml_template = '''
<source netmask="255.255.255.255" port="9995" ip="$host_ip"/>
<target port="9995" ip="10.6.56.15"/>
<target port="9991" ip="172.18.4.60"/>
<configText>$description</configText>'''

xml_close ='''
</flowfan>
<startup ports="9995"/>
</flowfan>'''

# host_list = [
#
#     {'host_ip': '192.168.1.1', 'desc': 'blah'},
#     {'host_ip': '192.168.1.2', 'desc': 'naw'}
#
# ]


def import_csv_data():
    '''Read data in CSV'''
    host_items = list()
    with open(csv_file, 'rb') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            host_items.append({
                'host_ip': row['host_ip'],
                'description': row['description']
            })
        return host_items


if __name__ == '__main__':

    host_list = import_csv_data()

    with open(ffan_file, 'w+') as f:
        f.write(xml_open)
        pos = 0
        for host in host_list:
            xml_dyn = Template(xml_template).substitute(host_list[pos])
            f.write(xml_dyn)
            pos+=1
        f.write(xml_close)
