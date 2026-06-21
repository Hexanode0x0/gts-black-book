---
icon: "lucide/toolbox"
tags:
    - "Tools"
    - "Generated"
---
# Generation
There are quite a few modding tools that generate things for the game. The following can be generated:

- [Grass Cache](./Grass Cache)
- [Terrain LOD](./Terrain LOD)
- [Object LOD](./Object LOD)

They all should be generated in the order they are listed in, but only if you're generating from scratch.

## Using MO2 To Capture Tool Output
Certain tools like xLODGen or Nemesis output directly into the data folder, and when used with Vortex, this output is extremely hard to package into a patch.

By using MO2 you can just to run the tools and easily capture the output into overwrite and create a mod from that.

Steps:

1. Have GTS installed and deployed in Vortex
2. Open MO2 on an empty profile
3. Run the tool with MO2 as per usual
4. The tool's output should appear in overwrite
5. Package what's in overwrite into a mod and use it in Vortex
