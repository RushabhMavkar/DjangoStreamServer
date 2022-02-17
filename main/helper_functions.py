import pyqrcode
import socket
import hashlib
import string
import random


def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def create_qrcode(port=8000):
    ip = get_ip()
    url = f"http://{ip}:{port}/"
    qr = pyqrcode.create(url)
    qr.svg("./main/static/main/assets/qrcode-dark.svg", module_color='#000', scale=8)
    qr.svg("./main/static/main/assets/qrcode-grey.svg", module_color='#828a91', scale=8)
    qr.svg("./main/static/main/assets/qrcode-light.svg", module_color='#fff', scale=8)
    return True


def generate_hash(length):
    sample_string = 'demostring'
    x = ''.join((random.choice(sample_string)) for x in range(length))
    return x
