from pathlib import Path



PROJECT_ROOT = Path(__file__).parent
UDP_SETTINGS = (PROJECT_ROOT / "Network/settings/udp.py")
print(UDP_SETTINGS)


PROJECT_ROOT = Path(__file__).parent
UDP_SERVER = (PROJECT_ROOT / "Network/udp.py")
print(UDP_SETTINGS)