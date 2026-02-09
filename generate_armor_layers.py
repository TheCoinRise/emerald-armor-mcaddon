#!/usr/bin/env python3
"""Generate armor layer textures for Minecraft Bedrock"""

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

# Colors
TRANSPARENT = (0, 0, 0, 0)
EMERALD_DARK = (0, 80, 40, 255)
EMERALD_MID = (0, 140, 70, 255)
EMERALD_LIGHT = (20, 180, 100, 255)
EMERALD_HIGHLIGHT = (80, 220, 140, 255)

def generate_layer_1():
    """Generate layer 1 texture (helmet, chestplate, boots) - 64x32"""
    width, height = 64, 32
    pixels = [[TRANSPARENT for _ in range(width)] for _ in range(height)]

    # Helmet (top-left quadrant, starts at 0,0)
    # Head top (8x8 at position 8,0)
    for y in range(8):
        for x in range(8, 16):
            pixels[y][x] = EMERALD_MID

    # Head front (8x8 at position 8,8)
    for y in range(8, 16):
        for x in range(8, 16):
            if y == 8:
                pixels[y][x] = EMERALD_HIGHLIGHT
            elif y < 12:
                pixels[y][x] = EMERALD_LIGHT
            else:
                pixels[y][x] = EMERALD_MID

    # Head right (8x8 at position 0,8)
    for y in range(8, 16):
        for x in range(0, 8):
            pixels[y][x] = EMERALD_MID

    # Head left (8x8 at position 16,8)
    for y in range(8, 16):
        for x in range(16, 24):
            pixels[y][x] = EMERALD_MID

    # Head back (8x8 at position 24,8)
    for y in range(8, 16):
        for x in range(24, 32):
            pixels[y][x] = EMERALD_DARK

    # Head bottom (8x8 at position 16,0)
    for y in range(8):
        for x in range(16, 24):
            pixels[y][x] = EMERALD_DARK

    # Chestplate body (starts at 16,16)
    # Body front (8x12 at position 20,20)
    for y in range(20, 32):
        for x in range(20, 28):
            if y == 20:
                pixels[y][x] = EMERALD_HIGHLIGHT
            elif y < 24:
                pixels[y][x] = EMERALD_LIGHT
            else:
                pixels[y][x] = EMERALD_MID

    # Body right (4x12 at position 16,20)
    for y in range(20, 32):
        for x in range(16, 20):
            pixels[y][x] = EMERALD_MID

    # Body left (4x12 at position 28,20)
    for y in range(20, 32):
        for x in range(28, 32):
            pixels[y][x] = EMERALD_MID

    # Body back (8x12 at position 32,20)
    for y in range(20, 32):
        for x in range(32, 40):
            pixels[y][x] = EMERALD_DARK

    # Body top (8x4 at position 20,16)
    for y in range(16, 20):
        for x in range(20, 28):
            pixels[y][x] = EMERALD_LIGHT

    # Arms (starts at 40,16)
    # Right arm (4x12 at position 44,20)
    for y in range(20, 32):
        for x in range(44, 48):
            pixels[y][x] = EMERALD_MID

    # Left arm outer
    for y in range(20, 32):
        for x in range(48, 52):
            pixels[y][x] = EMERALD_MID

    # Boots (at position 0,16 and 16,16 area - shares with legs in layer 2)
    # Boot front
    for y in range(26, 32):
        for x in range(4, 8):
            pixels[y][x] = EMERALD_MID

    for y in range(26, 32):
        for x in range(52, 56):
            pixels[y][x] = EMERALD_MID

    return create_png(width, height, pixels)

def generate_layer_2():
    """Generate layer 2 texture (leggings) - 64x32"""
    width, height = 64, 32
    pixels = [[TRANSPARENT for _ in range(width)] for _ in range(height)]

    # Leggings/pants area
    # Belt/waist area (at body position)
    for y in range(20, 24):
        for x in range(20, 28):
            pixels[y][x] = EMERALD_DARK

    for y in range(20, 24):
        for x in range(16, 20):
            pixels[y][x] = EMERALD_DARK

    for y in range(20, 24):
        for x in range(28, 32):
            pixels[y][x] = EMERALD_DARK

    # Right leg (4x12 at position 0,16)
    # Leg front
    for y in range(20, 32):
        for x in range(4, 8):
            if y < 24:
                pixels[y][x] = EMERALD_LIGHT
            else:
                pixels[y][x] = EMERALD_MID

    # Leg sides
    for y in range(20, 32):
        for x in range(0, 4):
            pixels[y][x] = EMERALD_MID

    for y in range(20, 32):
        for x in range(8, 12):
            pixels[y][x] = EMERALD_MID

    # Leg back
    for y in range(20, 32):
        for x in range(12, 16):
            pixels[y][x] = EMERALD_DARK

    # Left leg (mirror of right, at position 16,16 area)
    for y in range(20, 32):
        for x in range(20, 24):
            if y < 24:
                pixels[y][x] = EMERALD_LIGHT
            else:
                pixels[y][x] = EMERALD_MID

    for y in range(20, 32):
        for x in range(16, 20):
            pixels[y][x] = EMERALD_MID

    for y in range(20, 32):
        for x in range(24, 28):
            pixels[y][x] = EMERALD_MID

    for y in range(20, 32):
        for x in range(28, 32):
            pixels[y][x] = EMERALD_DARK

    return create_png(width, height, pixels)

def main():
    output_dir = "resource_pack/textures/models/armor"
    os.makedirs(output_dir, exist_ok=True)

    # Generate layer 1 (helmet, chestplate, boots)
    layer1_data = generate_layer_1()
    with open(os.path.join(output_dir, "emerald_layer_1.png"), 'wb') as f:
        f.write(layer1_data)
    print("Created emerald_layer_1.png")

    # Generate layer 2 (leggings)
    layer2_data = generate_layer_2()
    with open(os.path.join(output_dir, "emerald_layer_2.png"), 'wb') as f:
        f.write(layer2_data)
    print("Created emerald_layer_2.png")

if __name__ == "__main__":
    main()
