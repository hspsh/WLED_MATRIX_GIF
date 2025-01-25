import socket
import time

from PIL import Image
from PIL import ImageFilter, ImageEnhance

PIXEL_NUM = 4096
PACKET_LIMIT = 256

WLED_IP = "192.168.88.55"
GIF_FILE_PATH = r"polish.gif"
IMG_ENHANCE_LV = 2


def main():
    img = Image.open(GIF_FILE_PATH)
    for i in range(1, img.n_frames):
        img.seek(i)
        img.filter(ImageFilter.FIND_EDGES)

        resized = img.resize((64, 64))
        resized = ImageEnhance.Contrast(resized).enhance(IMG_ENHANCE_LV)
        image = [
            pixel[:3] for pixel in resized.getdata()
        ]
        show_image(image)


def show_image(image):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    offset = 0
    while offset < PIXEL_NUM:
        packet = build_packet(offset, image[offset:offset + PACKET_LIMIT])
        sock.sendto(packet, (WLED_IP, 21324))
        time.sleep(0.005)
        offset += PACKET_LIMIT


def build_packet(offset: int, pixels: list[list[int]], timeout: int = 5) -> bytes:
    header = [
        4,  # DNRGB
        timeout,
        (offset & 0xff00) >> 8,
        offset & 0xff,
    ]

    data = []
    for pixel in pixels:
        data.extend(pixel)

    return bytes(header + data)


if __name__ == "__main__":
    while True:
        main()
