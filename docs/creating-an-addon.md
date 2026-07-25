---
icon: "lucide/layers-plus"
tags: 
  - "Addon Collections"
  - "Tools"
---
# Creating An Addon
While creating a collection in Vortex is rather simple, addon collections are not officially supported and as such have some rough edges.

GTS is still is development, and therefore addons may need to update support newer versions. This can introduce a lot of maintenance overhead.

## Naming
Your addon should have 'GTS' in it's name. 'GTS' is preferred to 'Gate To Sovngarde' as most addons use 'GTS' and being in line with that will make your addon easier to find.

You should only use alphanumeric characters in the name of your addon (`A-Z` and `0-9`). Dashes and underscores (`-` and `_`) are also acceptable.

!!! danger
    Using special characters like `:`, `?`, `\`, or others may cause installation issues since Windows does not allow certain characters in file names.

## Scope
Before making an addon, you should consider it's scope, that meaning what your addons does, and what does it modify.

Addons like GTS Community Edition have a rather broad scope and as such tend to include a lot of disperate things, making them harder to maintain and increasing the surface area for bugs. 

On the other side of things, addons like GTS - True Light have a very narrow scope, and as such, are easier to maintain and check for bugs.

Generally, the smaller the scope and the less mods, the less of a maintenance burden your addon will be.

## Addon Page
Making a readable page for your addon is important if you want users to actually read it. There isn't a single best way of doing it, but you can have a look at what other addon's pages look like.

The easiest readable page to make is just bullet points. That's already much better than a wall of text.

When you're updating your addon, do not forget to update the page as well. Don't just add a note at the bottom, nodody will read that.

## Bad Plugin Groups
Certain addons, especially unmaintained ones, may come with messy plugin groups that can cause cycles or break the intended load order.

!!! warning
    Due to how collections work, this mess spreads. If you install an addon with bad groups, any addons you export will also contain them. Please practice safe and clean addon making.

To check if you're affected, go into the plugins tab and click 'Manage groups'. If your groups are a clean, straight line ending with 'Dynamic LOD', then you're fine and can stop reading.

If your install is dirty, follow these steps:

  1. Disable any and all addons in the mods tab
  2. Go into group management again
  3. Right-click on empty space and select reset
  4. Follow the [this guide on the GTS wiki](https://gatetosovngarde.wiki.gg/wiki/Resolving_Cycles) to set all GTS plugins into the right groups
  5. Re-export your collection, if you're an addon curator

## Custom Patches And Bundled Assets
Using bundled assets can be very convenient, but it's harder to maintain them in the long term.

The bundled assets can only be acquired by downloading the collection, they are very opaque and if somebody wants to replicate your addon on Wabbajack, they cannot do it if you're using a bundled asset. Bundled assets are much harder to version properly as well.

Making a small mod page for just uploading collection files is very common and encouraged over bundled assets.

!!! abstract "TL;DR"
    Do not use bundled assets and just upload your patch to Nexus.


## Breaking Things
Your first priority should be making sure that your addon is stable, and does not break any existing GTS features.

!!! warning
    If you have to break one or more GTS features for your addon to work, please document these explicitly on your collection's page.

You should avoid including mods with known crashes, that are outdated, or ones that conflict with GTS.

Testing things is very important, so make sure to do that whenever you add a mod to your addon.

## AE Upgrade
You should consider if and how your addon interacts with the AE Upgrade content.

If you wish to have the AE Upgrade be optional, like it is for GTS, add any mods that require the AE Upgrade as optional mods. Make sure to leave some instructions on your page to only install optional mods when the user has the AE Upgrade.

You can also avoid this problem by simply having the AE Upgrade as a requirement to use your addon.

## Mod Versioning
Vortex allows you to select 3 version settings for any mod you include in your collection, those being 'Prefer Exact', 'Exact Only', and 'Newest'.

Newer versions of Vortex default to 'Exact Only' and you should keep every mod on that specific setting. Having your mods on 'Prefer Exact' and 'Newest' can cause installation issues when those mods update.

!!! info
    'Prefer Exact' used to be the default, however, due to how Nexus is structured, it would end up behaving as 'Newest' the majority of the time.

## Redundancies
Ideally you should avoid making mods redundant, as it can cause confusion. If you do have to, make sure to mention it on your addon's page.

!!! tip
    Mods only become redundant when they're entirely overridden. Leaving just one file will get rid of the warning.

## Managing File Conflicts
Inevitably, you will encounter file conflicts as you make your addon. Vortex will replicate rules on user's setups so long as both mods are in your collection. This can cause issues when a mod your addon has conflicts with a GTS mod.

!!! danger
    Vortex does not ship rules for mods that are not directly in your addon. If you have a conflict between a mod in your addon and a GTS mod, the users will see this conflict as unresolved on their end, even if it's resolved on your end.

There are a few solutions to this, though they all have some drawback.

### Dependency Injection
One solution is to satisfy the requirement of having the mod in your addon. Add any conflicting GTS mods to your addon and Vortex will resolve rules properly. In GTS addons world, this is called dependency injection.

!!! warning
    If your mod conflicts with 'GTS - Specific Patches' or any other GTS patch, this method will lock your addon to a specific GTS version. This is because this file changes on every GTS update.

If GTS updates any mods that are injected into your addon, then Vortex will install two versions. The updated GTS one, and the old one in your addon, which will cause a lot of conflicts and require you to update the injected mod too. This is a mild concern since not that many mods in GTS frequently update.

!!! info
    This approach requires the highest amount of time, so it's discouraged if you don't intend on staying around to maintain your addon.

### Optional Mods
In a similar vein to dependency injection, you can include GTS mods as optional / recommended mods.

This has the advantage of doing all of what injection does, but when the mod in GTS updates, it won't cause as many conflicts as injection.

This approach has a few notable drawbacks:
  - You cannot use optional mods for AE Upgrade support
  - Any users that mistakenly install optional mods may encounter issues
  - The conflict remains anyway when GTS updates the mod, there just is less of them

This option exists, but is generally discouraged.

### Manual Resolution
Probably the best option for you as a curator, is to make a list of what conflicts your addon has and how to resolve them. This list should then be put on your addon's page.

!!! success "Recommended"
    This is the recommended option for conflicts. It makes it so your addon can persist though GTS updates without any effort from you. Though it does come at the cost of a more involved installation.

The only circumstance under which this approach breaks is when GTS adds new mods that conflict with what your addon has.

### Hybrid
If you wish to minimize the amount of manual rules users have to solve while installing, while keeping your addon reasonably future-proof, you can use dependacy injection on mods that are unlikely to update, and keep any other ones manual.

## Using SkyPatcher
There is a minor issue with SkyPatcher that causes Lucien's stats to be reset when loading a save. This issue can be mitigated by changing SkyPatcher's configuration, but if every addon had it's own, it would mean conflicts between all of them.

For this reason, all collections that need SkyPatcher should use the [GTS Addon Common Resource](https://www.nexusmods.com/skyrimspecialedition/mods/158815?tab=files) file from CE's resource repo. It contains the SkyPatcher configuration. Addons that use this file will not cause conflicts.

## Modifying GTS Plugins
This refers to modifying a plugin like 'GTS Patches - Quests.esp' and including it in your patch, overriding GTS' version.

!!! danger Shipping GTS Plugins
    Including GTS plugins in your addons is a bad idea, always. This will lock your addon to a specific GTS version, since those plugins change on every update. If a user updates GTS but your plugin is not updated, it can cause ==features to not work==, ==undebuggable crashes==, or even ==save corruption==.


You should not modify and ship your versions of GTS plugins, unless there is literally no other way for your addon to work.

## Reinstalling FOMODs
When you reinstall a GTS mod, change it's FOMOD options and include it in your addon, Vortex will reinstall the GTS mod. This will cause GTS, and any other addon, to appear incomplete.

!!! tip
    The incomplete warning can be disabled by setting the issue mod to be ignored in the collections tab. This can only be done on the user's end.

Make sure to include a note on your addon page that it will cause GTS to be incomplete.

## Mod Configuration Menu
MCM is managed with MCM Recorder. If you wish to change default MCM settings, this is how. Simply make your own recording and have it play after GTS' to override it's settings.

MCM Recorder playbacks are done in alphabetical order, so add a 'z' to your recording's name if it plays before GTS'.

Some MCMs cannot be changed with MCM Recorder. This is because they're managed by MCM Helper. MCM Helper menus have their own .ini configuration files, so change those instead.

!!! tip
    GTS uses MCM Unlocked and thus is not subject to the 128 MCM limit.

## Plugin Conflicts
Every time you add a mod, you should check if it's plugin is conflicting with any GTS ones by using xEdit.

If there are conflicts, you should forward the records in your custom patch, that way the load order is enforced by plugin masters.

This page will not cover how to use xEdit, as there are a few tutorials out there already.

!!! warning
    Plugin rules are subject to the same limitations as file conflict rules. You cannot have a rule referencing a plugin that's not in your collection.
