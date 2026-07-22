def define_env(env):
    env.variables["current_gts_version"] = 113
    # About Defining Addons:
        # You need to include all fields. Set the ones you don't want / have to an empty string ("") to not display them.
        # "name" => String. The name of the addon. Should match what's on Nexus.
        # "desc" => String. Description of the addon. Full Zensical markdown is supported, if a bit clunky.
        # "support" => String. lower case only. The support status of the addon. Use these variants:
            # "supported" - The addon is fully supported.
            # "out_of_date" - The addon needs to be updated.
            # "unsupported" - The curator does not offer any support or updates.
            # "deprecated" - Abandoned and has issues, this addon should not be used.
        # "versioning" => String. lower case only. How the addon is versioned against GTS. Use these variants:
            # "locked" - The addon is locked to a specific GTS version. If used with a "supported" status, the addon will be moved to 'out of date' automatically when GTS updates.
            # "minimum" - A minimum version of GTS is required.
            # "free" - No version restrictions.
        # "version_number" => Number. The GTS revision your addon is targeting. Will be used as minimum version for "locked" and "minimum" versioned addons. "free", "out_of_date", "unsupported", and "deprecated" addons will use it as a last confirmed working version.
        # "nexus_page" => String. Link to the collection's Nexus Mods page.
        # "nexus_page_tag" => String. Will be added to the link in parenthesis. Typically used to inform users that an addon is unlisted. e.g. "nexus_page_tag" = "Unlisted" => "Collection Page (Unlisted)"
        # "discord_channel" => String. Link to the discord channel (or thread) for an addon. If the addon doesn't have a dedicated channel, use Addons General.
        # "discord_channel_tag" => String. Same as "nexus_page_tag". Use it for specifying Addons General or a thread the addon uses, if it doesn't have a dedicated channel. e.g. "discord_channel_tag" = "Addons General" => "Discord Channell (Adddons General)"
        # "github" => String. Link to a Github repo.
        # "nsfw" => Bool. True or False. Is the addon sexual? True is only allowed in the 'cnn' group.
        # "not_compatible" => List of Strings. These will be added as bullet points in a collapsible box on the addon listing. e.g. "not_compatible" = ["Addon1", "Addon2"].

    #Large and unique
    env.variables["lnu_addons"] = [
        {
            "name": "GTS Community Edition",
            "desc": "GTS CE is a large addon that focuses on quality of life features, customizabilty, visuals, and more. It adds many new options to the Gear of Balance, overhauls Nordic Ruin exteriors, makes animals fluffy, adds tutorials, and a lot more.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/hvfynw",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424039315616301146",
            "discord_channel_tag": "",
            "github": "https://github.com/Hexanode0x0/GTS-Community-Edition",
            "nsfw": False,
            "not_compatible": ["Slow Your Roll... For GTS", "GOT - HOTD Dragons for GTS", "GTS Fluffworks"]
        },
        {
            "name": "GTS Legacy Lite",
            "desc": "Legacy Lite is a large addon that adds Legacy of the Dragonborn and a other supporting mods.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/p1eq2i",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424043173428199597",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "Smoking of Skooma for GTS",
            "desc": "Smoking of Skooma adds various pipe smoking options for Skooma, moon sugar, and elves ears.",
            "support": "supported",
            "versioning": "free",
            "version_number": 112,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/ht1rsj",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS - For the Love of Followers",
            "desc": "For the Love of Followers adds Nether's follower framework, and other follower enhancements.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/4j3ssn",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1495618864778575933",
            "discord_channel_tag": "Dibellan Arts Sheogorath Style",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Family Life",
            "desc": "Family Life adds a few family oriented mods.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/tohany",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "Slow Your Roll... for GTS",
            "desc": "Slow Your Roll adds Experience and various patches for it. It's outdated, abandoned, and superseded by GTS CE.",
            "support": "deprecated",
            "versioning": "free",
            "version_number": 98,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/exv627",
            "nexus_page_tag": "Unlisted",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424043123499204639",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["GTS Community Edition"]
        },
        {
            "name": "Roleplaying... in GTS",
            "desc": "Roleplaying... in GTS adds a variety of custom perk trees and ways to define your character.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/ockxzz",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Safe Save Lite",
            "desc": "GTS Unofficial Addon: Safe Save Lite adds some utility mods to make saves a bit safer.",
            "support": "supported",
            "versioning": "free",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/n6vlym",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
    ]
    #Visual and performance
    env.variables["vnp_addons"] = [
        {
            "name": "GTS - Brave Little Toaster Edition",
            "desc": "Brave Little Toaster is an addon that focuses on increasing performance at the cost of worse visuals.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 112,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/myqt2f",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS - Fabled Forests Lite 4 Toasters",
            "desc": "Fabled Forests Lite 4 Toasters replaces LODs with ones that are less performance intensive.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 110,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/emq9nj",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "Player Home Overhaul for GTS",
            "desc": "Player Home Overhaul changes existing houses in GTS.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 111,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/d1xsks",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GOT - HOTD Dragons for GTS",
            "desc": "GOT - HOTD Dragons changes the looks of dragons.",
            "support": "supported",
            "versioning": "free",
            "version_number": 91,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/vpyxkf",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["GTS Community Edition"]
        },
        {
            "name": "Runic Arts for GTS",
            "desc": "Runic Arts improves spell visuals.",
            "support": "supported",
            "versioning": "free",
            "version_number": 111,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/o9o7ol",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1486194390161424495",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Meshes++",
            "desc": "Meshes++ replaces various meshes with higher fideliy ones.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/u8cmpk",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS - True Light",
            "desc": "GTS - True Light replaces ELFX with True Light and Window Shadows Ultimate.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 111,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/ailix7",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS - Unofficial Visuals",
            "desc": "GTS - Unofficial Visuals is unsupported due to the curator being absent. It should still work, however.",
            "support": "unsupported",
            "versioning": "free",
            "version_number": 100,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/nhv91p",
            "nexus_page_tag": "",
            "discord_channel": "",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Fluffworks",
            "desc": "GTS Fluffworks adds fluff to animals with shell texturing. It's abandoned and superseded by GTS CE.",
            "support": "deprecated",
            "versioning": "minimum",
            "version_number": 94,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/xqwm5b",
            "nexus_page_tag": "Unlisted",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": ["GTS Community Edition"]
        },
    ]
    #Combat and magic
    env.variables["cnm_addons"] = [
        {
            "name": "Adamant Addons for GTS",
            "desc": "Adamant Addons for GTS adds new spells and combat options.",
            "support": "out_of_date",
            "versioning": "minimum",
            "version_number": 104,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/x2wcve",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424858532846637210",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["CuBoCorrx Combat Initiative for GTS", "GTS Black - Power Fantasy GTS"]
        },
        {
            "name": "Mannaz and Freyr for GTS",
            "desc": "Mannaz and Freyr for GTS adds Mannaz and Freyr for more racial bonuses and standing stone effects.",
            "support": "out_of_date",
            "versioning": "minimum",
            "version_number": 104,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/cda6ea",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424858532846637210",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "Modern Vanilla Combat (MVC) for GTS",
            "desc": "Modern Vanilla Combat (MVC) for GTS overhauls combat animations and behaviors.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 110,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/sxc4fu",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Honor In Death for GTS", "GTS Unofficial Addon: Motion Kombat", "CuBoCorrx Combat Initiative for GTS"]
        },
        {
            "name": "CuBoCorrx Combat Initiative for GTS",
            "desc": "CuBoCorrx Combat Initiative for GTS overhauls combat animations and behaviors.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/bm7kkx",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1495618864778575933",
            "discord_channel_tag": "Dibellan Arts Sheogorath Style",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Honor In Death for GTS", "GTS Unofficial Addon: Motion Kombat", "Modern Vanilla Combat (MVC) for GTS", "Blessed Perks for GTS", "GTS Black - Power Fantasy GTS", "Adamant Addons for GTS"]
        },
        {
            "name": "GTS Black - Power Fantasy GTS",
            "desc": "GTS Black - Power Fantasy GTS overhauls the perk trees and magic, making GTS much more of a power fantasy.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 104,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/giui1z",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424858532846637210",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Blessed Perks for GTS", "CuBoCorrx Combat Initiative for GTS", "Adamant Addons for GTS", "GTS Unofficial Spells", "GTS - Darenii's Spells"]
        },
        {
            "name": "Summermyst for GTS",
            "desc": "Summermyst for GTS brings in Summermyst and overhauls enchanting.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 104,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/2vhqbs",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424858532846637210",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Motion Kombat",
            "desc": "GTS Unofficial Addon: Motion Kombat reworks vanilla combat with new movement options.",
            "support": "out_of_date",
            "versioning": "minimum",
            "version_number": 104,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/8gir8y",
            "nexus_page_tag": "Unlisted",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Honor In Death for GTS", "Modern Vanilla Combat (MVC) for GTS", "CuBoCorrx Combat Initiative for GTS"]
        },
        {
            "name": "Honor In Death for GTS",
            "desc": "Honor In Death for GTS is a comprehensive combat overhaul with a lot of changes.",
            "support": "out_of_date",
            "versioning": "minimum",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/kwkfuj",
            "nexus_page_tag": "Unlisted",
            "discord_channel": "https://discord.com/channels/902984082181484615/1486194390161424495",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Modern Vanilla Combat (MVC) for GTS", "CuBoCorrx Combat Initiative for GTS", "GTS Unofficial Addon: Motion Kombat"]
        },
        {
            "name": "Blessed Perks for GTS",
            "desc": "Blessed Perks for GTS overhauls the perk trees to better serve the Honor in Death addon. It has been deprecated and will be merged into Honor in Death.",
            "support": "deprecated",
            "versioning": "locked",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/kojve0",
            "nexus_page_tag": "Unlisted",
            "discord_channel": "https://discord.com/channels/902984082181484615/1486194390161424495",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["GTS Black - Power Fantasy GTS", "CuBoCorrx Combat Initiative for GTS"]
        },
        {
            "name": "Creature Animations for GTS",
            "desc": "Creature Animations for GTS overhauls animations and movesets of creatures.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/oy6eak",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1486194390161424495",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS - Darenii's Spells",
            "desc": "GTS - Darenii's Spells adds various spells new spells. Since GTS v111, SkyPatcher, which is required for this addon, is no longer included. You'll have to install it manually or rely on another addon, like GTS CE.",
            "support": "unsupported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/h1b3nk",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": ["GTS - Unofficial Spells", "GTS Black - Power Fantasy GTS"]
        },
        {
            "name": "GTS - Unofficial Spells",
            "desc": "GTS - Unofficial Spells adds various spells new spells. This addon has an outdated version of SkyPatcher, and has been superseded by GTS - Darenii's Spells",
            "support": "deprecated",
            "versioning": "free",
            "version_number": 96,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/9puzyn",
            "nexus_page_tag": "",
            "discord_channel": "",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["GTS - Unofficial Spells", "GTS Black - Power Fantasy GTS"]
        },
        {
            "name": "GTS - DnD Guardians Addon",
            "desc": "GTS - DnD Guardians Addon adds the Dead and Daedric Guardians mod.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/mkmj3k",
            "nexus_page_tag": "",
            "discord_channel": "",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
    ]
    #Armor and weapons
    env.variables["anw_addons"] = [
        {
            "name": "Moar Armors for GTS",
            "desc": "Moar Armors for GTS adds new armors.",
            "support": "supported",
            "versioning": "free",
            "version_number": 112,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/0zynkf",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Armory for GTS (+BODY SWAP support)"]
        },
        {
            "name": "Civil War Armory for GTS",
            "desc": "Civil War Armory for GTS adds new armors for civil war factions.",
            "support": "supported",
            "versioning": "free",
            "version_number": 112,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/g4xsry",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Armory for GTS (+BODY SWAP support)"]
        },
        {
            "name": "Armory for GTS (+BODY SWAP support)",
            "desc": "Armory for GTS adds new armors for 3ba and himbo addons.",
            "support": "supported",
            "versioning": "free",
            "version_number": 112,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/vo9umm",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Civil War Armory for GTS", "Moar Armors for GTS"]
        },
        {
            "name": "GTS - Unofficial Armory",
            "desc": "GTS - Unofficial Armory adds new armors and weapons. It's unsupported due to the curator being absent, but it's likely to work fine.",
            "support": "unsupported",
            "versioning": "free",
            "version_number": 84,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/77lkfs",
            "nexus_page_tag": "",
            "discord_channel": "",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },

    ]
    #Interface and sound
    env.variables["ins_addons"] = [
        {
            "name": "Vel'dun UI for GTS",
            "desc": "Vel'dun UI for GTS overhauls the user interface to use Vel'dun UI and it adds lot of mods Vel'dun has compatibility with.",
            "support": "supported",
            "versioning": "free",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/veystx",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Kiza's Nordic UI for GTS", "GTS - Some Dragonborns need Gamepads", "GTS CE+ 21:9 Dragonborn UI", "GTS Unofficial Addon: Vanilla UI++"]
        },
        {
            "name": "Kiza's Nordic UI for GTS",
            "desc": "Kiza's Nordic UI for GTS overhauls the user interface to use Nordic UI and it adds a lot of mods Nordic UI has compatibility with.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/rjhvsf",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1492528267411062956",
            "discord_channel_tag": "Nordic UI Thread",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Vel'dun UI for GTS", "GTS - Some Dragonborns need Gamepads", "GTS CE+ 21:9 Dragonborn UI", "GTS Unofficial Addon: Vanilla UI++"]
        },
        {
            "name": "GTS - Some Dragonborns need Gamepads",
            "desc": "GTS - Some Dragonborns need Gamepads adds controller configuration, as well as the Dragonborn UI reskin.",
            "support": "supported",
            "versioning": "free",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/ajz80f",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Vel'dun UI for GTS", "Kiza's Nordic UI for GTS", "GTS CE+ 21:9 Dragonborn UI", "GTS Unofficial Addon: Vanilla UI++"]
        },
        {
            "name": "GTS CE+ 21:9 Dragonborn UI",
            "desc": "GTS CE+ 21:9 Dragonborn UI adds the Dragonborn UI reskin in a 21:9 aspect ratio.",
            "support": "supported",
            "versioning": "free",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/e6lvdc",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Vel'dun UI for GTS", "Kiza's Nordic UI for GTS", "GTS - Some Dragonborns need Gamepads", "GTS Unofficial Addon: Vanilla UI++"]
        },
        {
            "name": "GTS Unofficial Addon: Vanilla UI++",
            "desc": "GTS Unofficial Addon: Vanilla UI++ adds some UI and HUD elements in the vanilla interface style.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/hahyis",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Vel'dun UI for GTS", "Kiza's Nordic UI for GTS", "GTS - Some Dragonborns need Gamepads", "GTS CE+ 21:9 Dragonborn UI"]
        },
        {
            "name": "GTS Unofficial Addon: DBVO Talion",
            "desc": "GTS Unofficial Addon: DBVO Talion adds the Talion player character voice over.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/py5gf3",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: More Music",
            "desc": "GTS Unofficial Addon: More Music adds a variety of music to the game.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/ll4pnu",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Ambient Sounds",
            "desc": "GTS Unofficial Addon: Ambient Sounds adds a variety of ambient and environmental audio.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/lzztpj",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS CE+ Music Addon",
            "desc": "GTS CE+ Music Addon adds The Northern Diaries and OrganicView's music.",
            "support": "supported",
            "versioning": "free",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/qllf3p",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Sweet Immersion Breaking Clarity",
            "desc": "GTS Sweet Immersion Breaking Clarity various tags to books and dialogue to tell which mods they're from.",
            "support": "supported",
            "versioning": "free",
            "version_number": 110,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/1mgdgk",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1495618864778575933",
            "discord_channel_tag": "Dibellan Arts Sheogorath Style",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
    ]
    #Quest and land
    env.variables["qnl_addons"] = [
        {
            "name": "Daughter of Coldharbour, SDA in GTS.",
            "desc": "Daughter of Coldharbour brings in Serana Dialogue Addon, Ashe, and Improved Follower Dialogue Lydia.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 112,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/cskwke",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS – Glenmoril & Unslaad Expansion",
            "desc": "GTS – Glenmoril & Unslaad Expansion adds the two Vicn quest mods that are not already present in GTS.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 110,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/tqztnh",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS - The Rot Below",
            "desc": "GTS - The Rot Below adds The Rot Below quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 100,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/o61o2j",
            "nexus_page_tag": "",
            "discord_channel": "",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS - Unofficial Followers",
            "desc": "GTS - Unofficial Followers adds Follower Dialogue Expansion mods. It is unsupported due to the absence of the curator, but it should work fine.",
            "support": "unsupported",
            "versioning": "free",
            "version_number": 104,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/c51zyc",
            "nexus_page_tag": "",
            "discord_channel": "",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Beyond Reach",
            "desc": "GTS Unofficial Addon: Beyond Reach adds the Beyond Reach quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/hqnfby",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Gray Cowl",
            "desc": "GTS Unofficial Addon: Gray Cowl adds the The Gray Cowl of Nocturnal - 10th anniversary quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/jvftwi",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Valefrost",
            "desc": "GTS Unofficial Addon: Valefrost adds the Valefrost quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/eqae2z",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Midnight Sun",
            "desc": "GTS Unofficial Addon: Midnight Sun adds the Midnight Sun quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/2x1n9v",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Clockwork",
            "desc": "GTS Unofficial Addon: Clockwork adds the Clockwork quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 102,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/5c1g1b",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Olenveld",
            "desc": "GTS Unofficial Addon: Olenveld adds the Olenveld quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/uiqcd7",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Chain of Time",
            "desc": "GTS Unofficial Addon: Chain of Time adds the Chain of Time quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/oye75r",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Vominheim",
            "desc": "GTS Unofficial Addon: Vominheim adds the Vominheim quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 102,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/runfg3",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Falskaar",
            "desc": "GTS Unofficial Addon: Falskaar adds the Falskaar quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 102,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/su3ckv",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Summerset Isle",
            "desc": "GTS Unofficial Addon: Summerset Isle adds the Summerset Isle quest mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/evfiqz",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS Unofficial Addon: Sidequests",
            "desc": "GTS Unofficial Addon: Sidequests adds various quest mods made by Nimwraith and wSkeever.",
            "support": "supported",
            "versioning": "free",
            "version_number": 111,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/x5axps",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS - Unofficial Quests",
            "desc": "GTS - Unofficial Quests adds various quest mods made by wSkeever. It's unsupported due to the curator being absent, though the addon should still work fine.",
            "support": "unsupported",
            "versioning": "free",
            "version_number": 84,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/lv0g2o",
            "nexus_page_tag": "",
            "discord_channel": "",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
    ]
    #Character and nsfw
    env.variables["cnn_addons"] = [
        {
            "name": "Beauty Salon for GTS",
            "desc": "Beauty Salon for GTS adds high poly head and a lot of character creation options.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 112,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/ej5p4q",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1518756996906614919",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["GTS Character Creation Add-On"]
        },
        {
            "name": "GTS SkyRev Skins SFW",
            "desc": "GTS SkyRev Skins SFW changes the skin of characters to Skysights and Reverie.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 105,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/d95tzv",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["Bits and Pieces for GTS - BNP SFW", "GTS - Simple Bodies SkyRev NSFW", "GTS - Simple Bodies - BNP NSFW", "GTS - 3BA Dat Body", "GTS - Dibellan Arts Sheogorath Style"]
        },
        {
            "name": "Bits and Pieces for GTS - BNP SFW",
            "desc": "Bits and Pieces for GTS - BNP SFW changes the skin of characters to Bits and Pieces.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 107,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/lnpzep",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": ["GTS SkyRev Skins SFW", "GTS - Simple Bodies SkyRev NSFW", "GTS - Simple Bodies - BNP NSFW", "GTS - 3BA Dat Body", "GTS - Dibellan Arts Sheogorath Style"]
        },
        {
            "name": "Just 3BA for GTS (NSFW)",
            "desc": "Just 3BA for GTS changes the female body to 3ba.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 112,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/t29mgm",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1518756996906614919",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": True,
            "not_compatible": ["GTS Unofficial Addon: Nude Bodies", "GTS - Simple Bodies - BNP NSFW", "GTS - Simple Bodies SkyRev NSFW", "Body Swap updated", "GTS - 3BA Dat Body", "GTS - Dibellan Arts Sheogorath Style"]
        },
        {
            "name": "GTS Unofficial Addon: Nude Bodies (NSFW)",
            "desc": "GTS Unofficial Addon: Nude Bodies changes bodies to TNG and BHUNP.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 108,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/pu2rfl",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": True,
            "not_compatible": ["Just 3BA for GTS", "GTS - Simple Bodies - BNP NSFW", "GTS - Simple Bodies SkyRev NSFW", "Body Swap updated", "GTS - 3BA Dat Body", "GTS - Dibellan Arts Sheogorath Style"]
        },
        {
            "name": "GTS - Simple Bodies - BNP NSFW",
            "desc": "GTS - Simple Bodies - BNP NSFW changes skins to BNP.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 105,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/kabujw",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": True,
            "not_compatible": ["Just 3BA for GTS", "GTS - Simple Bodies - BNP SFW", "GTS SkyRev Skins SFW", "GTS - Simple Bodies SkyRev NSFW", "Body Swap updated", "GTS - 3BA Dat Body", "GTS - Dibellan Arts Sheogorath Style"]
        },
        {
            "name": "GTS - Simple Bodies SkyRev NSFW",
            "desc": "GTS - Simple Bodies SkyRev NSFW changes skins to Reverie and Skysights.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 105,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/jqvxxb",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": True,
            "not_compatible": ["Just 3BA for GTS", "GTS - Simple Bodies - BNP SFW", "GTS SkyRev Skins SFW", "GTS - Simple Bodies - BNP NSFW", "Body Swap updated", "GTS - 3BA Dat Body", "GTS - Dibellan Arts Sheogorath Style"]
        },
        {
            "name": "Body Swap updated (NSFW)",
            "desc": "Body Swap updated changes bodies to 3ba and himbo.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/xa2h3u",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1495618864778575933",
            "discord_channel_tag": "Dibellan Arts Sheogorath Style Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": ["Just 3BA for GTS", "GTS - Simple Bodies - BNP SFW", "GTS SkyRev Skins SFW", "GTS - Simple Bodies - BNP NSFW", "GTS - Simple Bodies - SkyRev NSFW", "GTS - 3BA Dat Body", "GTS - Dibellan Arts Sheogorath Style"]
        },
        {
            "name": "GTS Unofficial Addon: OStim+Quests (NSFW)",
            "desc": "GTS Unofficial Addon: OStim+Quests adds Ostim and some supporting quests.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 102,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/pm8mrj",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424038554232946689",
            "discord_channel_tag": "Addons General",
            "github": "",
            "nsfw": True,
            "not_compatible": ["Dibellan Arts - Ostim for GTS", "GTS - Dibellan Arts Sheogorath Style", "Sheogorath Style lite", "Dat Body - Snu Snu"]
        },
        {
            "name": "Dibellan Arts - Ostim for GTS (NSFW)",
            "desc": "Dibellan Arts - Ostim for GTS adds Ostim.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 102,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/wp5yr1",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424055746458423347",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": True,
            "not_compatible": ["GTS Unofficial Addon: OStim+Quests", "GTS - Dibellan Arts Sheogorath Style", "Sheogorath Style lite", "Dat Body - Snu Snu"]
        },
        {
            "name": "GTS - Dibellan Arts Sheogorath Style (NSFW)",
            "desc": "Dibellan Arts - Ostim for GTS adds Ostim and it's own body mods.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/nuwfgt",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1495618864778575933",
            "discord_channel_tag": "Dibellan Arts Sheogorath Style Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": ["GTS Unofficial Addon: OStim+Quests", "Dibellan Arts - Ostim for GTS", "Sheogorath Style lite", "Dat Body - Snu Snu"]
        },
        {
            "name": "Sheogorath Style lite (NSFW)",
            "desc": "Sheogorath Style lite adds Ostim.",
            "support": "supported",
            "versioning": "minimum",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/01lzad",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1495618864778575933",
            "discord_channel_tag": "Dibellan Arts Sheogorath Style Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": ["GTS Unofficial Addon: OStim+Quests", "Dibellan Arts - Ostim for GTS", "GTS - Dibellan Arts Sheogorath Style", "Dat Body - Snu Snu"]
        },
        {
            "name": "GTS-M'rissi-A Sheogorath Style Addon (NSFW)",
            "desc": "GTS-M'rissi-A Sheogorath Style Addon adds the M'rissi follower and Ostim for them.",
            "support": "supported",
            "versioning": "free",
            "version_number": 109,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/u3euhv",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1495618864778575933",
            "discord_channel_tag": "Dibellan Arts Sheogorath Style Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": []
        },
        {
            "name": "GTS ODF for Body Swap (NSFW)",
            "desc": "GTS ODF for Body Swap adds Overlay Distribution Framework support for body swap.",
            "support": "supported",
            "versioning": "free",
            "version_number": 110,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/db2x6o",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1495618864778575933",
            "discord_channel_tag": "Dibellan Arts Sheogorath Style Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": []
        },
        {
            "name": "GTS - Fairies (NSFW)",
            "desc": "GTS - Fairies adds the fairies mod.",
            "support": "supported",
            "versioning": "free",
            "version_number": 111,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/eykfps",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1495618864778575933",
            "discord_channel_tag": "Dibellan Arts Sheogorath Style Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": []
        },
        {
            "name": "Sheo Style presents PSBoss (NSFW)",
            "desc": "Sheo Style presents PSBoss adds various mods by PSBoss.",
            "support": "supported",
            "versioning": "free",
            "version_number": 113,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/0gmvov",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1495618864778575933",
            "discord_channel_tag": "Dibellan Arts Sheogorath Style Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": []
        },
        {
            "name": "GTS Character Creation Add-On",
            "desc": "GTS Character Creation Add-On has been abandoned and superseded by Beauty Salon for GTS.",
            "support": "deprecated",
            "versioning": "minimum",
            "version_number": 86,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/o0uiqd",
            "nexus_page_tag": "",
            "discord_channel": "",
            "discord_channel_tag": "",
            "github": "",
            "nsfw": False,
            "not_compatible": []
        },
        {
            "name": "GTS - 3BA Dat Body (NSFW)",
            "desc": "GTS - 3BA Dat Body has been abandoned and superseded by other addons.",
            "support": "deprecated",
            "versioning": "locked",
            "version_number": 89,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/th259l",
            "nexus_page_tag": "Unlisted",
            "discord_channel": "https://discord.com/channels/902984082181484615/1224423423737073704",
            "discord_channel_tag": "NSFW Discussions Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": ["Just 3BA for GTS", "GTS - Simple Bodies - BNP SFW", "GTS SkyRev Skins SFW", "GTS - Simple Bodies - BNP NSFW", "GTS - Simple Bodies - SkyRev NSFW", "Body Swap Updated", "GTS - Dibellan Arts Sheogorath Style"]
        },
        {
            "name": "Dat Body - Snu Snu (NSFW)",
            "desc": "Dat Body - Snu Snu has been abandoned and superseded by other addons.",
            "support": "deprecated",
            "versioning": "locked",
            "version_number": 89,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/zg5tiw",
            "nexus_page_tag": "Unlisted",
            "discord_channel": "https://discord.com/channels/902984082181484615/1224423423737073704",
            "discord_channel_tag": "NSFW Discussions Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": ["GTS Unofficial Addon: OStim+Quests", "Dibellan Arts - Ostim for GTS", "Sheogorath Style lite", "GTS - Dibellan Arts Sheogorath Style (NSFW)"]
        },
        {
            "name": "GTS - Varric NPC Replacers (NSFW)",
            "desc": "GTS - Varric NPC Replacers is abandoned and relies on Dat Body, which is deprecated.",
            "support": "deprecated",
            "versioning": "locked",
            "version_number": 89,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/zg5tiw",
            "nexus_page_tag": "Unlisted",
            "discord_channel": "https://discord.com/channels/902984082181484615/1224423423737073704",
            "discord_channel_tag": "NSFW Discussions Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": []
        },
        {
            "name": "Dat Body - Additions (NSFW)",
            "desc": "Dat Body - Additions is abandoned and relies on Dat Body, which is deprecated.",
            "support": "deprecated",
            "versioning": "locked",
            "version_number": 89,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/bpttqt",
            "nexus_page_tag": "Unlisted",
            "discord_channel": "https://discord.com/channels/902984082181484615/1224423423737073704",
            "discord_channel_tag": "NSFW Discussions Thread",
            "github": "",
            "nsfw": True,
            "not_compatible": []
        },
    ]
    #display code
    @env.macro
    def list_addons(addons_to_list, current_gts_version):
        return f"""
```python exec="on"\n
these_addons = {addons_to_list}
current_gts_version = {current_gts_version}
""" + r"""

supported_addons = []
out_of_date_addons = []
unsupported_addons = []
deprecated_addons = []

def print_addon_generics(addon):
    if addon["nsfw"] == True:
        print("\t:lucide-triangle-alert: This addon is NSFW. Viewer discretion is advised.\n")

    if addon["nexus_page"] != "":
        nexus_string = ""
        if addon["nexus_page_tag"] != "":
            nexus_string = nexus_string + f"[:lucide-file-text: Collection Page ({addon["nexus_page_tag"]})]"
        else:
            nexus_string = nexus_string + "[:lucide-file-text: Collection Page]"
        nexus_string = nexus_string + f"({addon["nexus_page"]})"
        print("\t" + nexus_string + "\n")
    else:
        print(f"\t:lucide-circle-x: This addon is not currently available.")

    if addon["discord_channel"] != "":
        discord_string = ""
        if addon["discord_channel_tag"] != "":
            discord_string = discord_string + f"[:fontawesome-brands-discord: Discord Channel ({addon["discord_channel_tag"]})]"
        else:
            discord_string = discord_string + "[:fontawesome-brands-discord: Discord Channel]"
        discord_string = discord_string + f"({addon["discord_channel"]})"
        print("\t" + discord_string + "\n")

    if addon["github"] != "":
        print(f"\t[:octicons-mark-github-24: GitHub Repo]({addon["github"]})\n")

    if addon["not_compatible"] != []:
        print(f"\t??? danger \"Incompatibilities\"\n")
        print(f"\t\tAddons are usually incompatible when they touch the same area, or have some mods that overlap.\n\n\t\tThe following are not compatible with {addon["name"]}:\n")
        for incompat in addon["not_compatible"]:
            print(f"\t\t- {incompat}")

for addon in these_addons:
    if addon["support"] == "deprecated":
        deprecated_addons.append(addon)
    elif addon["support"] == "unsupported" and addon["versioning"] == "locked" and addon["version_number"] != current_gts_version:
        deprecated_addons.append(addon)
    elif addon["support"] == "out_of_date":
        out_of_date_addons.append(addon)
    elif addon["support"] == "unsupported":
        unsupported_addons.append(addon)
    elif addon["support"] == "supported" and addon["versioning"] == "locked" and addon["version_number"] == current_gts_version:
        supported_addons.append(addon)
    elif addon["support"] == "supported" and addon["versioning"] == "locked" and addon["version_number"] != current_gts_version:
        out_of_date_addons.append(addon)
    elif addon["support"] == "supported":
        supported_addons.append(addon)
    else:
        continue

if len(supported_addons) > 0:
    print("## Supported Addons\n Addons listed here are supported by their respective curators, and expected to work.\n\n")
    for addon in supported_addons:

        print(f"??? success \"{addon["name"]}\"\n")
        print(f"\t**{addon["desc"]}**\n")
        print(f"\t:lucide-info: {addon["name"]} is supported.\n")

        if addon["versioning"] == "locked":
            print(f"\t:lucide-lock: {addon["name"]} only works with GTS v{addon["version_number"]} and will need to update if GTS updates.\n")
        elif addon["versioning"] == "minimum":
            print(f"\t:lucide-target: {addon["name"]} requires at minimum GTS v{addon["version_number"]} and is very likely to work with future GTS updates.\n")
        elif addon["versioning"] == "free":
            print(f"\t:lucide-lock-open: {addon["name"]} is very likely to work with past or future GTS versions. It was last fully tested with GTS v{addon["version_number"]}\n")

        print_addon_generics(addon)

if len(out_of_date_addons) > 0:
    print("## Out Of Date Addons\n Addons listed here are supported by their respective curators, but have not yet been updated to support the newest GTS version.\n\n")
    for addon in out_of_date_addons:

        print(f"??? question \"{addon["name"]}\"\n")
        print(f"\t**{addon["desc"]}**\n")
        print(f"\t:lucide-info: {addon["name"]} is in the process of being updated. It was last confirmed working with with GTS v{addon["version_number"]}.\n")

        if addon["versioning"] == "locked":
            print(f"\t:lucide-lock: {addon["name"]} only works with GTS v{addon["version_number"]}.\n")

        print_addon_generics(addon)

if len(unsupported_addons) > 0:
    print("## Unsupported Addons\n Addons listed here are not supported by their respective curators. They may or may not work.\n\n")
    for addon in unsupported_addons:

        print(f"??? warning \"{addon["name"]}\"\n")
        print(f"\t**{addon["desc"]}**\n")
        print(f"\t:lucide-info: {addon["name"]} was last confirmed working with with GTS v{addon["version_number"]}.\n")

        if addon["versioning"] == "locked":
            print(f"\t:lucide-lock: {addon["name"]} only works with GTS v{addon["version_number"]}.\n")
        elif addon["versioning"] == "minimum":
            print(f"\t:lucide-target: {addon["name"]} requires at minimum GTS v{addon["version_number"]}.\n")
        elif addon["versioning"] == "free":
            print(f"\t:lucide-lock-open: {addon["name"]} is likely to work with past or future GTS versions.\n")

        print_addon_generics(addon)

if len(deprecated_addons) > 0:
    print("## Deprecated Addons\n Addons listed here are abandoned and have severe issues. They should not be used.\n\n")
    for addon in deprecated_addons:

        print(f"??? failure \"{addon["name"]}\"\n")
        print(f"\t**{addon["desc"]}**\n")
        print(f"\t:lucide-info: {addon["name"]} was last confirmed working with with GTS v{addon["version_number"]}.\n")

        if addon["versioning"] == "locked":
            print(f"\t:lucide-lock: {addon["name"]} only works with GTS v{addon["version_number"]}.\n")
        else:
            print(f"\t:lucide-ban: Version information for {addon["name"]} is limited to the known last working version.\n")

        print_addon_generics(addon)
```
        """
    env.macro(list_addons, "list_addons")
