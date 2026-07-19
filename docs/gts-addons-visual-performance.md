---
icon: "lucide/star"
tags:
    - "Addon Collections"
    - "Visual"
---
# Visual & Performance Addons
This page lists addons that improve visuals or increase performance.

The current version of GTS is v{{ current_gts_version }}

```python exec="on"
#comes from include directory
these_addons = {{ vnp_addons }}
current_gts_version = {{ current_gts_version }}

supported_addons = []
out_of_date_addons = []
unsupported_addons = []
deprecated_addons = []

def print_addon_generics(addon):   
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
