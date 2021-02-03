# All credits Goes to https://github.com/XiaomiFirmwareUpdater/xiaomi_uranus_chatbot
# https://github.com/XiaomiFirmwareUpdater/xiaomi_uranus_chatbot

import yaml
import requests
import json


async def load_specs_data():
    """
    fetch Xiaomi devices models
    """
    warner_stark = requests.get(url="https://raw.githubusercontent.com/XiaomiFirmwareUpdater/xiaomi_devices/gsmarena/devices.json").text
    specs = json.loads(warner_stark)
    return specs


async def get_specs(device, specs_data):
    try:
        info = [i for i in specs_data if device == i['codename']][0]
    except IndexError:
        return
    data = {}
    name = info['name']
    url = info['url']
    details = info['specs']
    device_status = details['Launch'][0]['Status']
    network = details['Network'][0]['Technology']
    weight = details['Body'][0]['Weight']
    display = details['Display'][0]['Type'] + '\n' + details['Display'][0]['Size'] + '\n' + \
              details['Display'][0]['Resolution']
    chipset = details['Platform'][0]['Chipset'] + '\n' + details['Platform'][0]['CPU'] + '\n' + \
              details['Platform'][0]['GPU']
    memory = details['Memory'][0]['Internal']
    main_cam = details['Main Camera'][0]
    camera, camera_details = next(iter(main_cam.items()))
    main_cam = f"{camera} {camera_details}"
    front_cam = details['Selfie camera'][0]
    camera, camera_details = next(iter(front_cam.items()))
    front_cam = f"{camera} {camera_details}"
    jack = details['Sound'][0]['3.5mm jack']
    usb = details['Comms'][0]['USB']
    sensors = details['Features'][0]['Sensors']
    battery = details['Battery'][0]['info']
    charging = None
    try:
        charging = details['Battery'][0]['Charging']
    except KeyError:
        pass
    data.update({'name': name, 'url': url, 'status': device_status, 'network': network,
                 'weight': weight, 'display': display, 'chipset': chipset, 'memory': memory,
                 'rear_camera': main_cam, 'front_camera': front_cam, 'jack': jack,
                 'usb': usb, 'sensors': sensors, 'battery': battery})
    if charging:
        data.update({'charging': charging})
    return data
    
async def load_roms_data():
    """
    load recovery ROMs data form MIUI tracker yaml file
    :returns data - a list with latest updates
    """
    ws = requests.get(url="https://raw.githubusercontent.com/XiaomiFirmwareUpdater/miui-updates-tracker/master/data/latest.yml").text
    roms = yaml.load(ws)
    return roms


async def get_miui(device, method, updates):
    """ Get miui from for a device """
    return [i for i in updates if i['codename'].split('_')[0] == device and i['method'] == method]


async def diff_miui_updates(new, old):
    """ diff miui updates to get the changes """
    changes = {}
    if not old:
        return changes
    for item in new:
        for old_item in old:
            if old_item['codename'] == item['codename'] and item['version'] != old_item['version']:
                is_new = None
                if "V" in item['version'] and "V" in old_item['version']:  # miui stable
                    new_version_array = item['version'].split('.')
                    old_version_array = old_item['version'].split('.')
                    if new_version_array[-1][0] > old_version_array[-1][0]:
                        is_new = True  # new android version
                    elif int(new_version_array[0][1:]) > int(old_version_array[0][1:]):
                        is_new = True  # new miui version
                    elif int(new_version_array[1]) > int(old_version_array[1]):
                        is_new = True  # new miui sub-version
                    elif int(new_version_array[2]) > int(old_version_array[2]):
                        is_new = True  # new miui minor version
                elif "V" not in item['version'] and "V" not in old_item['version'] \
                        and item['version'][0].isdigit() and old_item['version'][0].isdigit():  # miui weekly
                    new_version_array = item['version'].split('.')
                    old_version_array = old_item['version'].split('.')
                    if int(new_version_array[0]) > int(old_version_array[0]):
                        is_new = True
                    elif int(new_version_array[1]) > int(old_version_array[1]):
                        is_new = True
                    elif int(new_version_array[2]) > int(old_version_array[2]):
                        is_new = True
                if is_new:
                    codename = item['codename'].split('_')[0]
                    try:
                        if changes[codename]:
                            changes.update({codename: changes[codename] + [item]})
                    except KeyError:
                        # when a new device is added
                        changes.update({codename: [item]})
    if changes:
        DIFF_LOGGER.info(f"MIUI changes:\n{str(changes)}")
    return changes
    
    
    
    
    
