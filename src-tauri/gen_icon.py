#!/usr/bin/env python3
"""Generate placeholder icons for Tauri app."""

from PIL import Image, ImageDraw, ImageFont
import os

ICON_DIR = os.path.dirname(os.path.abspath(__file__))
COLORS = {
    'primary': '#667eea',
    'secondary': '#764ba2',
    'white': '#ffffff'
}

def create_icon(size, filename):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    margin = size // 8
    radius = size // 6
    
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=radius,
        fill=COLORS['primary']
    )
    
    font_size = size // 3
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "URL"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (size - text_w) // 2 - bbox[0]
    y = (size - text_h) // 2 - bbox[1]
    
    draw.text((x, y), text, fill=COLORS['white'], font=font)
    
    img.save(os.path.join(ICON_DIR, filename))
    print(f"Created {filename} ({size}x{size})")

def create_ico():
    sizes = [16, 32, 48, 64, 128, 256]
    images = []
    for size in sizes:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        margin = size // 8
        radius = size // 6
        draw.rounded_rectangle(
            [margin, margin, size - margin, size - margin],
            radius=radius,
            fill=COLORS['primary']
        )
        font_size = max(size // 3, 10)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        text = "URL"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = (size - text_w) // 2 - bbox[0]
        y = (size - text_h) // 2 - bbox[1]
        draw.text((x, y), text, fill=COLORS['white'], font=font)
        images.append(img)
    
    ico_path = os.path.join(ICON_DIR, 'icon.ico')
    images[0].save(ico_path, sizes=[(img.size[0], img.size[1]) for img in images], append_images=images[1:])
    print(f"Created icon.ico")

def create_icns():
    img = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    margin = 128
    radius = 85
    draw.rounded_rectangle(
        [margin, margin, 1024 - margin, 1024 - margin],
        radius=radius,
        fill=COLORS['primary']
    )
    try:
        font = ImageFont.truetype("arial.ttf", 300)
    except:
        font = ImageFont.load_default()
    text = "URL"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (1024 - text_w) // 2 - bbox[0]
    y = (1024 - text_h) // 2 - bbox[1]
    draw.text((x, y), text, fill=COLORS['white'], font=font)
    
    icns_path = os.path.join(ICON_DIR, 'icon.icns')
    img.save(icns_path)
    print(f"Created icon.icns")

if __name__ == '__main__':
    create_icon(32, '32x32.png')
    create_icon(128, '128x128.png')
    create_icon(256, '128x128@2x.png')
    create_ico()
    create_icns()
    print("All icons generated!")
