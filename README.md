# ComfyUI_Limited: A Lightweight Alternative

Get started with ComfyUI Limited, a stripped-down alternative to run your [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that meets the minimum requirements for a quick and lightweight graph interface experience. Just like a workflow viewer.

## Why Limited Mode?

Using ComfyUI as a workflow viewer can indeed be valuable for various users and developers if it has support for custom nodes. This demo showcase Limited, a lightweight method to run ComfyUI. 
It's ideal for situations where you need to quickly access the graph interface without the overhead of the full ComfyUI.
That said, this demo is capable of loading workflows with custom nodes and without the installation of requirements as fast as possible to restart, same as a workflow viewer.
You can modify the script to suit your needs, like letting certain modules to load for dev purposes.

## Features

- Lightweight: ComfyUI Limited requires minimal resources, making it suitable for testing and development environments.
- Fast: Load the graph interface quickly, without the overhead of the full ComfyUI.
- Utilizes common practices: ComfyUI Limited uses test-driven development practices to ensure compatibility with your existing ComfyUI setup.
- Compatibility: ComfyUI Limited do not modify your current ComfyUI setup and updates, including custom nodes updates.

## Limitations

- No image generation: ComfyUI Limited does not support generating images.
- Limited custom node support: I'm testing a limited list of custom nodes. If you have more installed, they may load, but may not function as expected.
- Limited error handling: ComfyUI Limited may ignore some error messages, so be aware of this limitation.

## Requirements

- Python 3.x
- aiohttp
- git for windows

## Installation

Copy limited.py to the root directory of your current ComfyUI installation, next to main.py

## Installation from scratch

1. Lightweight Clone ComfyUI repository and ComfyUI-Manager (recommended):
    ```sh
    git clone --depth 1 --filter=blob:none https://github.com/comfyanonymous/ComfyUI
    cd ComfyUI\custom_nodes
    git clone --depth 1 --filter=blob:none https://github.com/ltdrdata/ComfyUI-Manager
    ```

2. Install the minimum required dependency package in a virtual environment:
    ```sh
    python -s -m pip install aiohttp
    ```

3. Copy limited.py to the root directory of your ComfyUI installation, next to main.py

## Usage

Run ComfyUI Limited like this, change port if you want (or make a bat file):
```sh
python -s limited.py --cpu --windows-standalone-build --port 8189
```

### Arguments

- `-s`: Run python with disable the import of the site module.
- `--cpu`: use cpu, not gpu
- `--port`: custom port, allow to free standard ComfyUI port 8188.
- `--windows-standalone-build`: open the web browser when ready.

## Uninstallation

- Delete limited.py file.
- Delete limited_modules.log file

## Code Overview

### `whitelist` list

Contains the modules this script should not prevent its load.

### `modules_to_mock` list

Contains the blacklist of modules to prevent its load by using a dummy module.

### `DEBUG` variable

Show on console whenever installation of modules gets ignored.

### `NO_INSTALLS` variable

Extra code to prevent installations from custom nodes by alternative methods.

## Important Notes

- ComfyUI Limited is intended for graphical user interface use only, so you won't be able to generate images.
- ComfyUI Limited now supports dynamically loading custom nodes, provided they aren’t too complex.
- Keep in mind that ComfyUI Limited is a stripped-down instance of ComfyUI, and all features not related to graph nodes will not be available.

## Tested Custom Nodes:
- ltdrdata [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- rgthree [rgthree-comfy](https://github.com/rgthree/rgthree-comfy)
- yolain [ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use) *
- Suzie1 [ComfyUI_Comfyroll_CustomNodes](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes) *
- shiimizu [ComfyUI_smZNodes](https://github.com/shiimizu/ComfyUI_smZNodes) *
- pythongosssss [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
- giriss [comfy-image-saver](https://github.com/giriss/comfy-image-saver) (deprecated repo, switch to alexoplus' fork instead)
- alexoplus [ComfyUI-Image-Saver](https://github.com/alexopus/ComfyUI-Image-Saver)
- 54rt1n [ComfyUI-DareMerge](https://github.com/54rt1n/ComfyUI-DareMerge)
- jags111 [efficiency-nodes-comfyui](https://github.com/jags111/efficiency-nodes-comfyui) *
- WASasquatch [was-node-suite-comfyui](https://github.com/WASasquatch/was-node-suite-comfyui)
- ZHO-ZHO-ZHO [ComfyUI-BRIA_AI-RMBG](https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG)
- TinyTerra [ComfyUI_tinyterraNodes](https://github.com/TinyTerra/ComfyUI_tinyterraNodes)
- Nourepide [ComfyUI-Allor](https://github.com/Nourepide/ComfyUI-Allor) *
- ltdrdata [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- crystian [ComfyUI-Crystools](https://github.com/crystian/ComfyUI-Crystools) *
- Fannovel16 [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) *
- cubiq [ComfyUI_IPAdapter_plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus)
- spacepxl [ComfyUI-Florence-2](https://github.com/spacepxl/ComfyUI-Florence-2)
- Acly [comfyui-inpaint-nodes](https://github.com/Acly/comfyui-inpaint-nodes)
- EllangoK [ComfyUI-post-processing-nodes](https://github.com/EllangoK/ComfyUI-post-processing-nodes)
- cubiq [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)
- chflame163 [ComfyUI_LayerStyle](https://github.com/chflame163/ComfyUI_LayerStyle) *
- BadCafeCode [masquerade-nodes-comfyui](https://github.com/BadCafeCode/masquerade-nodes-comfyui)
- receyuki [comfyui-prompt-reader-node](https://github.com/receyuki/comfyui-prompt-reader-node)
- M1kep [ComfyLiterals](https://github.com/M1kep/ComfyLiterals)
- WASasquatch [ComfyUI_Preset_Merger](https://github.com/WASasquatch/ComfyUI_Preset_Merger)
- filliptm [ComfyUI_Fill-Nodes](https://github.com/filliptm/ComfyUI_Fill-Nodes)
- ssitu [ComfyUI_UltimateSDUpscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale)
- Ttl [ComfyUi_NNLatentUpscale](https://github.com/Ttl/ComfyUi_NNLatentUpscale)
- huchenlei [ComfyUI-layerdiffuse](https://github.com/huchenlei/ComfyUI-layerdiffuse) *
- BlenderNeko [ComfyUI_ADV_CLIP_emb](https://github.com/BlenderNeko/ComfyUI_ADV_CLIP_emb)
- comfyanonymous [ComfyUI_experiments](https://github.com/comfyanonymous/ComfyUI_experiments)
- bvhari [ComfyUI_ImageProcessing](https://github.com/bvhari/ComfyUI_ImageProcessing)
- Jcd1230 [rembg-comfyui-node](https://github.com/Jcd1230/rembg-comfyui-node)
- Loewen-Hob [rembg-comfyui-node-better](https://github.com/Loewen-Hob/rembg-comfyui-node-better)
- Mamaaaamooooo [batchImg-rembg-ComfyUI-nodes](https://github.com/Mamaaaamooooo/batchImg-rembg-ComfyUI-nodes)
- Derfuu [Derfuu_ComfyUI_ModdedNodes](https://github.com/Derfuu/Derfuu_ComfyUI_ModdedNodes)
- fssorc [ComfyUI_FaceShaper](https://github.com/fssorc/ComfyUI_FaceShaper)
- Acly [comfyui-tooling-nodes](https://github.com/Acly/comfyui-tooling-nodes)

  (* the complexity of this custom nodes required extra effort)

## Acknowledgments

I would like to thank the original authors of ComfyUI for their work and the contributors to the custom nodes for their contributions to the ComfyUI ecosystem.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
