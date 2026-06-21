---
icon: "lucide/mountain-snow"
tags:
    - "Tools"
    - "LOD"
    - "Generated"
    - "Landscape"
    - "Visual"
---
# Terrain LOD
Terrain LOD is generated with [xLODGen - Terrain](https://stepmodifications.org/forum/topic/13451-xlodgen-terrain-lod-beta-132-for-fnv-fo3-fo4-fo4vr-tes5-sse-tes5vr-enderal-enderalse/). When you move away from terrain and it disappears or does not match the terrain that was there before, that's a terrain LOD issue.

!!! danger
    Install xLODGen to a dedicated directory, and do not mix it with xEdit.

You'll also need [SSE Terrain Tamriel Extend](https://www.nexusmods.com/skyrimspecialedition/mods/54680), but only for generating terrain LOD. It should be disabled after.

You can run xLODGen from Vortex just fine, but be sure to set the following arguments: `-sse` and `-o:"{output path}"`. You should, of course, replace '{output path}' with the path to wherever you want the output to be generated.

!!! tip
    The output path should preferably be set to a directory that's directly on a drive, to avoid permission issues.

    Example: `-o:"C:\xLODGen_output\"`. Be sure to actually create the directory, and make sure it's empty.

## Before Generation
Disable GTS' xLOD Terrain file.

Temporarily remove any and all content from the AE Upgrade. Only Fishing, Rare Curios, Survival Mode, and Saints & Seducers are to stay.

!!! tip
    The file names for the creations that should stay are:
    
    - ccbgssse001-Fish.esm
    - ccbgssse037-curios.esl
    - ccbgssse025-advdsgs.esm
    - ccqdrsse001-survivalmode.esl

All GTS AE content should also be disabled. You can easily find it by searching "Anniversary Edition Upgrade".

## xLODGen Settings
The following settings should be used for terrain LOD generation for GTS. Unless you have a reason to do so, you should replicate these exactly.

* Objects LOD: **false**
* Trees LOD: **false**
* Terrain LOD: **true**
* Occlusion: **false**
---
* Height Maps: **true**
* Bake normal-maps: **true**
* Bake specular: **false**
* Vertex Color Intensity: **1.00**
* Default size Diffuse: **16**
* Normal: **16**
* Seasons: **Default, WIN**

Be sure to set the settings for all LOD distances.

### LOD 4 Settings
???+ abstract "LOD 4 Settings"
    **Meshes:**
    
    - Quality: **4**
    - Max Vertices: **32767**
    - Optimize Unseen: **false**
    - Protect Borders: **true**
    - Hide Quads: **false**

    **Diffuse:**

    - Size: **512**
    - Format: **DXT1**
    - MipMap: **true**
    - Brightness: **0**
    - Contrast: **0**
    - Gamma: **1.15**
  
    **Normal:**
    
    - Size: **512**
    - Format: **DXT1**
    - MipMap: **false**
    - Raise steepness: **false**

### LOD 8 Settings
???+ abstract "LOD 8 Settings"
    **Meshes:**
    
    - Quality: **8**
    - Max Vertices: **32767**
    - Optimize Unseen: **550**
    
    **Diffuse:**
    
    - Size: **256**
    - Format: **DXT1**
    - MipMap: **false**
    - Brightness: **0**
    - Contrast: **0**
    - Gamma: **1.15**
    
    **Normal:**
    
    - Size: **256**
    - Format: **DXT1**
    - MipMap: **false**
    - Raise steepness: **false**

### LOD 16 Settings
???+ abstract "LOD 16 Settings"
      **Meshes:**
      
      - Quality: **8**
      - Max Vertices: **32767**
      - Optimize Unseen: **550**
    
      **Diffuse:**
      
      - Size: **256**
      - Format: **DXT1**
      - MipMap: **false**
      - Brightness: **0**
      - Contrast: **0**
      - Gamma: **1.15**
    
      **Normal:**
      
      - Size: **256**
      - Format: **DXT1**
      - MipMap: **false**
      - Raise steepness: **false**
    
### LOD 32 Settings
???+ abstract "LOD 32 Settings"
    **Meshes:**
    
    - Quality: **4**
    - Max Vertices: **32767**
    - Optimize Unseen: **550**
  
    **Diffuse:**
    
    - Size: **256**
    - Format: **DXT1**
    - MipMap: **false**
    - Brightness: **0**
    - Contrast: **0**
    - Gamma: **1.15**
  
    **Normal:**
    
    - Size: **256**
    - Format: **DXT1**
    - MipMap: **false**
    - Raise steepness: **false**

## After Generation

After xLODGen is done, go to your output folder and package it like a regular mod.

Remember to disable SSE Terrain Tamriel Extend and re-enable GTS' xLOD Terrain file once you're done. Your mod should be overriding GTS LODs.

Un-remove the AE content, unless you're also generating [Object LOD](./Object LOD).
