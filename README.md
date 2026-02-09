# Emerald Armor Addon

A Minecraft Bedrock Edition addon that adds powerful Emerald Armor - **10x stronger than Diamond!**

## Features

- **4 Armor Pieces**: Helmet, Chestplate, Leggings, Boots
- **10x Diamond Protection**: Massively increased defense values
- **10x Diamond Durability**: 3,630 - 5,280 durability per piece
- **Green Emerald Textures**: Beautiful green armor design
- **Craftable**: Made from Cobblestone
- **Repairable**: Repair with Emeralds at an anvil
- **Built-in Fire Resistance**: Reduced damage from fire, lava, and magma

## Armor Stats

| Piece | Protection | Durability | Diamond Comparison |
|-------|------------|------------|-------------------|
| Helmet | 30 | 3,630 | 10x (Diamond: 3, 363) |
| Chestplate | 80 | 5,280 | 10x (Diamond: 8, 528) |
| Leggings | 60 | 4,950 | 10x (Diamond: 6, 495) |
| Boots | 30 | 4,290 | 10x (Diamond: 3, 429) |
| **Total** | **200** | - | Diamond Total: 20 |

## Crafting Recipes

Craft using **Cobblestone** in standard armor patterns:

```
Helmet:          Chestplate:      Leggings:        Boots:
E E E            E   E            E E E
E   E            E E E            E   E            E   E
                 E E E            E   E            E   E
```

## Installation

1. **Download** both folders or create a `.mcaddon` file
2. **Double-click** the `.mcaddon` file, or:
   - Copy `behavior_pack` to: `%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\behavior_packs\`
   - Copy `resource_pack` to: `%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\resource_packs\`
3. **Activate** both packs in your world settings
4. **Enable** "Holiday Creator Features" in Experiments (for custom items)

## Commands

Get the armor set instantly (requires cheats enabled):

```
/function give_emerald_armor
```

Enchant equipped armor with Fire Protection, Feather Falling, Depth Strider, Soul Speed:

```
/function enchant_armor
```

Or give individual pieces:

```
/give @s emerald:emerald_helmet
/give @s emerald:emerald_chestplate
/give @s emerald:emerald_leggings
/give @s emerald:emerald_boots
```

## Recommended Enchantments

The armor is designed to be enchanted with:
- **Fire Protection IV** - All pieces
- **Feather Falling IV** - Boots
- **Depth Strider III** - Boots
- **Soul Speed III** - Boots

Use `/function enchant_armor` after equipping to apply all enchantments.

## Compatibility

- Minecraft Bedrock Edition 1.20.0+
- Windows 10/11, Xbox, PlayStation, Switch, Mobile
- Requires "Holiday Creator Features" experimental toggle

## Creating .mcaddon File

To create a single installable file:

1. Select both `behavior_pack` and `resource_pack` folders
2. Add to a ZIP archive
3. Rename from `.zip` to `.mcaddon`
4. Double-click to install

## License

Free to use and modify. Credit appreciated but not required.
