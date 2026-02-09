# Enchant the item you are HOLDING in your hand
# Hold each armor piece and run: /function enchant_held

# Fire Protection IV (all armor)
enchant @s fire_protection 4

# Feather Falling IV (boots only - will fail silently on other pieces)
enchant @s feather_falling 4

# Depth Strider III (boots only)
enchant @s depth_strider 3

# Soul Speed III (boots only)
enchant @s soul_speed 3

# Protection IV (general protection)
enchant @s protection 4

# Unbreaking III
enchant @s unbreaking 3

tellraw @s {"rawtext":[{"text":"§aEnchantments applied to held item!"}]}
