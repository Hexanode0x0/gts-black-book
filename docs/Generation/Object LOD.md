---
icon: "lucide/castle"
tags:
    - "Tools"
    - "LOD"
    - "Generated"
    - "Landscape"
    - "Visual"
---
# Object LOD
Object LOD is generated with [DynDOLOD](https://www.nexusmods.com/skyrimspecialedition/mods/68518). When you get far away from an object and it disappears or changes shape, that's an LOD issue.

This page assumes you're more or less familiar with DynDOLOD. If you're not, you can read [it's documentation](https://dyndolod.info).

Before generating LODs, you should make sure your [grass cache](./Grass Cache.md) and [terrain LOD](./Terrain LOD.md) are in order.

## Before Generation
Temporarily remove any and all content from the AE Upgrade. Only Fishing, Rare Curios, Survival Mode, and Saints & Seducers are to stay.

!!! tip
    The file names for the creations that should stay are:
    
    - ccbgssse001-Fish.esm
    - ccbgssse037-curios.esl
    - ccbgssse025-advdsgs.esm
    - ccqdrsse001-survivalmode.esl

Disable GTS' DynDOLOD and Texgen outputs.

Run xEdit's Quick Auto Clean on Update.esm, Dawnguard.esm, and HearthFires.esm

Disable DynDOLOD loading screens by adding the line `AddLoadScreens=0` to the \[DynDOLOD] section in `DynDOLOD\Edit Scripts\DynDOLOD_SSE.ini`

Enable generation in Bruma by removing 'BSHeartland (Tamriel) - bsheartland.esm' from `DynDOLOD\Edit Scripts\DynDOLOD\Configs\DynDOLOD_SSE_worldspace_ignore.txt`

## Texgen
Run Texgen with Vortex.

The output path should preferably be set to a directory that's directly on a drive, to avoid permission issues. Example: `C:\Texgen_output\`. Be sure to actually create the directory, and make sure it's empty.

### Texgen Settings
Stitched Object LOD Textues: True

  - Base Size: 256

---
Rendered Object LOD Textures: True

  - Base Size: 256

---
Tree/Grass LOD Billboards: True

  - Untis per pixel: 11.0
  - Texture size Min: 32
  - Max: 1024
  - Grass: True
    - Direct: 100
    - Ambient 80
  - HD Grass: False
  - Tree: True
    - Direct: 90
    - Ambient: 65
  - HD Tree: True
    - Direct: 90
    - Ambient: 65
    - Smoothness: 30
  - Rendered: True
    - Direct: 100
    - Ambient: 55
    - Smoothenss: 0
---
- Diffuse alpha: BC3 (DXT5)
- Diffuse: BC1 (DXT1)
- Normal specular: BC3 (DXT5)
- Normal: BC1 (DXT1)

### Texgen Output
Create a mod from the Texgen output and install it.

## Generating LODs for GTS
Start DynDOLOD and select advanced mode.

The output path should preferably be set to a directory that's directly on a drive, to avoid permission issues. Example: `C:\DynDOLOD_output\`. Be sure to actually create the directory, and make sure it's empty.

### Worldspaces
Select both FXGlow and Candles.

Make sure all worldspaces are selected, with the exception of the following:

- aaaMBWerewolfNightmareWorld
- aaaMBworld
- BSKHyorkerIsle
- ksws07World
- zDcdGhostSea
- zDcdDwemereth
- zDcdBlindRealm

### Mesh and Reference Rules
The only changes from default are to the tree rules. Set it to the following:

- LOD Level 4: Billboard1
- LOD Level 8: Billboard4
- LOD Level 16: Billboard1
- LOD Level 32: Billboard6
- Flags: VWD, TREE
- Grid: NearLOD
- Reference: Unchanged

### Options
Set the following settings in the options section.

#### Object LOD

  - Object LOD: True
  - Level 32: False
  - Max tile size LOD: 1024
  - Max tile size full: 256

#### Tree LOD

  - Tree LOD: False
  - Ultra: True
  - Large: False
  - Billboard brightness: 0
  - Max tile size billboard: 1024

#### Dynamic LOD

  - Dynamic LOD: True
  - NearGridToLoad: 11
  - FarGridToLoad: 21

#### Occlusion Data

  - Occlusion data: True
  - Quality: 3
  - Plugin: True

#### Terrain Underside

  - Terrain underside: True
  - Quality: 8
  - Height: 500

#### Grass LOD

  - Grass LOD: True
  - Density: 60%
  - Mode: 1

#### Lights

  - Glow windows: True
  - High: True
  - Fake lights selected world: False
  - Fake lights child world: True

#### Seasons

  - Seasons: True
    - Default, WIN
  - Snow: False

#### References

  - Prefer base record LOD assignments over rules: False
  - Upgrade NearGrid large references to FarGrid: True
  - Large reference bugs workaround: Forced True
  - Downgrade FarGrid references to NearGrid: False
  - Parent > child: True
  - Child > parent: Low

### DynDOLOD Output
Create a mod from the DynDOLOD output and install it.
