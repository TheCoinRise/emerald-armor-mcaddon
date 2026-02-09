#!/usr/bin/env python3
"""Generate green emerald armor textures for Minecraft Bedrock"""

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

    # PNG signature
    signature = b'\x89PNG\r\n\x1a\n'

    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    ihdr = png_chunk(b'IHDR', ihdr_data)

    # IDAT chunk (image data)
    raw_data = b''
    for row in pixels:
        raw_data += b'\x00'  # filter byte
        for r, g, b, a in row:
            raw_data += bytes([r, g, b, a])

    compressed = zlib.compress(raw_data, 9)
    idat = png_chunk(b'IDAT', compressed)

    # IEND chunk
    iend = png_chunk(b'IEND', b'')

    return signature + ihdr + idat + iend

# Colors
EMERALD_DARK = (0, 100, 50, 255)
EMERALD_MID = (0, 168, 84, 255)
EMERALD_LIGHT = (80, 220, 140, 255)
EMERALD_HIGHLIGHT = (150, 255, 180, 255)
TRANSPARENT = (0, 0, 0, 0)

# Helmet pattern (16x16)
helmet_pattern = [
    "................",
    "....LLLLLL......",
    "...LMMMMMML.....",
    "..LMMMMMMMMM....",
    "..LMHHMMMHMML...",
    "..LMMMMMMMMMML..",
    "..LMMMMMMMMML...",
    ".LMMMMMMMMMML...",
    ".LMMMMMMMMMMML..",
    ".LDDMMMMMMDDL...",
    ".LDDDDDDDDDDDL..",
    "..LDDDDDDDDDL...",
    "..LLLLLLLLLL....",
    "................",
    "................",
    "................",
]

# Chestplate pattern (16x16)
chestplate_pattern = [
    "................",
    ".LLLL....LLLL...",
    "LMMML....LMMML..",
    "LMMMLLLLLLMMML..",
    "LMMMMMMMMMMMML..",
    "LMHMMMMMMMMHML..",
    ".LMMMMMMMMMML...",
    ".LMMMMMMMMMML...",
    "..LMMMMMMMMML...",
    "..LMMMMMMMMML...",
    "..LMMMMMMMML....",
    "...LMMMMMMML....",
    "...LDDDDDDDL....",
    "....LDDDDL......",
    ".....LLLL.......",
    "................",
]

# Leggings pattern (16x16)
leggings_pattern = [
    "................",
    "..LLLLLLLLLL....",
    "..LMMMMMMMMML...",
    "..LMHMMMMHMML...",
    "..LMMMMMMMMML...",
    "..LMMMMMMMMML...",
    "..LMML..LMML....",
    "..LMML..LMML....",
    "..LMML..LMML....",
    "..LMML..LMML....",
    "..LMML..LMML....",
    "..LDML..LMDL....",
    "..LDDL..LDDL....",
    "..LLLL..LLLL....",
    "................",
    "................",
]

# Boots pattern (16x16)
boots_pattern = [
    "................",
    "................",
    "................",
    "................",
    "................",
    "...LLL...LLL....",
    "...LMML..LMML...",
    "...LMML..LMML...",
    "...LMML..LMML...",
    "..LMMML.LMMML...",
    "..LMMMMLMMMML...",
    ".LMMMMMLMMMMML..",
    ".LDDDDDLDDDDL...",
    ".LLLLLLLLLLL....",
    "................",
    "................",
]

def pattern_to_pixels(pattern):
    """Convert pattern string to pixel array"""
    color_map = {
        '.': TRANSPARENT,
        'L': EMERALD_DARK,
        'M': EMERALD_MID,
        'H': EMERALD_HIGHLIGHT,
        'D': EMERALD_DARK,
    }
    pixels = []
    for row in pattern:
        pixel_row = [color_map.get(c, TRANSPARENT) for c in row]
        pixels.append(pixel_row)
    return pixels

def main():
    output_dir = "resource_pack/textures/items"
    os.makedirs(output_dir, exist_ok=True)

    textures = {
        "emerald_helmet.png": helmet_pattern,
        "emerald_chestplate.png": chestplate_pattern,
        "emerald_leggings.png": leggings_pattern,
        "emerald_boots.png": boots_pattern,
    }

    for filename, pattern in textures.items():
        pixels = pattern_to_pixels(pattern)
        png_data = create_png(16, 16, pixels)
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(png_data)
        print(f"Created {filepath}")

    print("\nAll textures generated successfully!")

if __name__ == "__main__":
    main()
