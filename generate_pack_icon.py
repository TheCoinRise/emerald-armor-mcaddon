#!/usr/bin/env python3
"""Generate pack icon for Emerald Armor addon"""

import struct
import zlib
import os

def create_png(width, height, pixels):
    """Create a PNG file from pixel data"""
    def png_chunk(chunk_type, data):
        chunk_len = struct.pack('>I', len(data))
        chunk_data = chunk_type + data
        crc = struct.pack('>I', zlib.crc32(chunk_data) & 0xffffffff)
        return chunk_len + chunk_data + crc

    signature = b'\x89PNG\r\n\x1a\n'
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    ihdr = png_chunk(b'IHDR', ihdr_data)

    raw_data = b''
    for row in pixels:
        raw_data += b'\x00'
        for r, g, b, a in row:
            raw_data += bytes([r, g, b, a])

    compressed = zlib.compress(raw_data, 9)
    idat = png_chunk(b'IDAT', compressed)
    iend = png_chunk(b'IEND', b'')

    return signature + ihdr + idat + iend

# 64x64 emerald-themed pack icon
def generate_pack_icon():
    size = 64
    pixels = []

    for y in range(size):
        row = []
        for x in range(size):
            # Create emerald gem pattern
            cx, cy = size // 2, size // 2
            dx, dy = abs(x - cx), abs(y - cy)

            # Diamond/gem shape
            if dx + dy < 28:
                # Inner gradient
                dist = dx + dy
                if dist < 8:
                    # Bright center highlight
                    color = (150, 255, 180, 255)
                elif dist < 16:
                    # Mid emerald
                    color = (0, 200, 100, 255)
                elif dist < 24:
                    # Darker emerald
                    color = (0, 140, 70, 255)
                else:
                    # Edge
                    color = (0, 100, 50, 255)
            elif dx + dy < 30:
                # Dark border
                color = (0, 60, 30, 255)
            else:
                # Transparent background
                color = (0, 0, 0, 0)

            row.append(color)
        pixels.append(row)

    return create_png(size, size, pixels)

def main():
    icon_data = generate_pack_icon()

    # Save to both packs
    for pack in ['behavior_pack', 'resource_pack']:
        filepath = os.path.join(pack, 'pack_icon.png')
        with open(filepath, 'wb') as f:
            f.write(icon_data)
        print(f"Created {filepath}")

if __name__ == "__main__":
    main()
