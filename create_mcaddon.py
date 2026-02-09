#!/usr/bin/env python3
"""Create a proper .mcaddon ZIP file for Minecraft Bedrock"""

import zipfile
import os

def create_mcaddon():
    addon_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(addon_dir, "EmeraldArmor.mcaddon")

    # Remove old file if exists
    if os.path.exists(output_file):
        os.remove(output_file)

    # Create ZIP file
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add behavior_pack
        bp_dir = os.path.join(addon_dir, "behavior_pack")
        for root, dirs, files in os.walk(bp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, addon_dir)
                # Use forward slashes for ZIP compatibility
                arc_name = arc_name.replace('\\', '/')
                zf.write(file_path, arc_name)
                print(f"Added: {arc_name}")

        # Add resource_pack
        rp_dir = os.path.join(addon_dir, "resource_pack")
        for root, dirs, files in os.walk(rp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, addon_dir)
                # Use forward slashes for ZIP compatibility
                arc_name = arc_name.replace('\\', '/')
                zf.write(file_path, arc_name)
                print(f"Added: {arc_name}")

    print(f"\nCreated: {output_file}")
    print(f"Size: {os.path.getsize(output_file)} bytes")

if __name__ == "__main__":
    create_mcaddon()
