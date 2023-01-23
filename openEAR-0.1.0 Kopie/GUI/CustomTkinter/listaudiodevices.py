import pyaudio

#Liest alle verfügbaren Audio-Geräte aus und schreibt diese in eine Liste

## Update: Teams wird nun nicht mehr als Audioquelle angezeigt


def get_input_devices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    devices = []
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0 and p.get_device_info_by_host_api_device_index(0,i).get('name') != "Microsoft Teams Audio":
            device_info = p.get_device_info_by_host_api_device_index(0, i)
            device = (device_info.get('index'), device_info.get('name'))
            devices.append(device)

    return devices
