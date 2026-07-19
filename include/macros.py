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
        # "not_compatible" => List of Strings. These will be added as bullet points in a collapsible box on the addon listing. e.g. "not_compatible" = ["Addon1", "Addon2"].

    #Large and unique
    env.variables["lnu_addons"] = [
        {
            "name": "GTS Community Edition",
            "desc": "GTS CE is a large addon that focuses on quality of life features, customizabilty, visuals, and more. It adds many new options to the Gear of Balance, overhauls Nordic Ruin exteriors, makes animals fluffy, adds tutorials, and a lot more.",
            "support": "supported",
            "versioning": "locked",
            "version_number": 112,
            "nexus_page": "https://www.nexusmods.com/games/skyrimspecialedition/collections/hvfynw",
            "nexus_page_tag": "",
            "discord_channel": "https://discord.com/channels/902984082181484615/1424039315616301146",
            "discord_channel_tag": "",
            "github": "https://github.com/Hexanode0x0/GTS-Community-Edition",
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
            "not_compatible": ["GTS Community Edition"]
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
            "not_compatible": ["CuBoCorrx Combat Initiative for GTS", "GTS Black - Power Fantasy GTS"]
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
            "not_compatible": ["GTS - Unofficial Spells", "GTS Black - Power Fantasy GTS"]
        },
    ]
