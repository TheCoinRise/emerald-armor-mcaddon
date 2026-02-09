# Give full Emerald Armor set
# Use: /function give_emerald_armor

give @s emerald:emerald_helmet 1
give @s emerald:emerald_chestplate 1
give @s emerald:emerald_leggings 1
give @s emerald:emerald_boots 1

tellraw @s {"rawtext":[{"text":"§a§lEmerald Armor received!"},{"text":"\n§7To enchant: Hold each piece and run /function enchant_held"}]}
