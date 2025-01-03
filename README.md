# gentle-socket-io

[![Changelog](https://img.shields.io/github/v/release/ubiros-dev/gentle-socket-io?include_prereleases&label=changelog)](https://github.com/ubiros-dev/gentle_socket_io/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ubiros-dev/gentle-socket-io/blob/main/LICENSE)

Socket communication with Ubiros Gentle Grippers

## Installation

Install this library using `pip`:
```bash
pip install git+https://github.com/ubiros-dev/gentle_socket_io.git
```
## Usage

```python
from gentle_socket_io.GentleSocket import GentleSocket
from gentle_socket_io.GentleProfile import GentleProfile

gentle = GentleSocket(numFingers=3)

hostGripper = "hostname.local"  #Enter hostname or IP address of your Ubiros Gentle gripper
gentle.initialize(hostGripper)

print('Profile Name:', gentle.defaultProfile.name)
print('Finger Pos:', gentle.fingerPos)

appleProfile = GentleProfile(name = "apple", force = 2500, open = 30, close = 80)           #define parameters to pick up apples in a single profile
bananaProfile = GentleProfile(name = "banana", force = 1200, open = 40, close = 70)
eggProfile = GentleProfile(name = "Egg", force = 900, open = 40, close = 60, vmax=80)

gentle.changeProfile(appleProfile)      #change object profile to pick up apples

gentle.open()       #open fingers to the predefined percentage of the selected profile

#execute image processing

#execute robot motion

gentle.close()      #close fingers to the predefined percentage level of the selected profile

gentle.moveFinger(60)   #move all fingers to 60% level

gentle.moveFinger(70, 1)    #move finger 1 to 70% level
```

