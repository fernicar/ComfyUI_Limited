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

## Limitations

- No image generation: ComfyUI Limited does not support generating images.
- Limited custom node support: ComfyUI Limited only supports 24 custom nodes. If you have more installed, they may load, but may not function as expected.
- Limited error handling: ComfyUI Limited may ignore some error messages, so be aware of this limitation.

## Requirements

- Python 3.x
- aiohttp
- git

## Installation

1. Clone ComfyUI repository:
    ```sh
    git clone https://github.com/comfyanonymous/ComfyUI
    cd ComfyUI
    ```

2. Install the required package in a virtual environment:
    ```sh
    python -s -m pip install aiohttp
    ```

3. Copy limited.py to the root directory of your ComfyUI installation, next to main.py

4. Run limited.py instead of main.py:
    ```sh
    python -s limited.py --cpu --windows-standalone-build --port 8189
    ```

## Usage

Run ComfyUI limited, change port if you want:
```sh
python -s limited.py --cpu --windows-standalone-build --port 8189
```

### Arguments

- `-s`: Run python with disable the import of the site module.
- `--cpu`: use cpu, no gpu
- `--port`: custom port, allow to free standard ComfyUI port 8188.
- `--windows-standalone-build`: open the web browser when ready.

## Uninstallation

- Delete limited.py file.

## Code Overview

### `whitelist` list

Contains the modules this script should not block its load.

### `modules_to_mock` list

Contains the blacklist of modules to block its load by using a dummy module.

### `DEBUG` variable

Show on console whenever installation of modules gets ignored.

### `NO_INSTALLS` variable

Extra code to prevent installations from custom nodes by alternative methods.

## Important Notes

- ComfyUI Limited is intended for graphical user interface use only, so you won't be able to generate images.
- Currently, ComfyUI Limited only supports 5 custom nodes. If you have more installed, they will load, but may not function as expected.
- Keep in mind that ComfyUI Limited is a stripped-down instance of ComfyUI, and all features not related to graph nodes will not be available.

## Supported Custom Node list:
- ltdrdata [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- rgthree [rgthree-comfy](https://github.com/rgthree/rgthree-comfy)
- yolain [ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use)
- Suzie1 [ComfyUI_Comfyroll_CustomNodes](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes)
- shiimizu [ComfyUI_smZNodes](https://github.com/shiimizu/ComfyUI_smZNodes)
- pythongosssss [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
- giriss [comfy-image-saver](https://github.com/giriss/comfy-image-saver)
- 54rt1n [ComfyUI-DareMerge](https://github.com/54rt1n/ComfyUI-DareMerge)
- jags111 [efficiency-nodes-comfyui](https://github.com/jags111/efficiency-nodes-comfyui)
- WASasquatch [was-node-suite-comfyui](https://github.com/WASasquatch/was-node-suite-comfyui)
- ZHO-ZHO-ZHO [ComfyUI-BRIA_AI-RMBG](https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG)
- TinyTerra [ComfyUI_tinyterraNodes](https://github.com/TinyTerra/ComfyUI_tinyterraNodes)
- Nourepide [ComfyUI-Allor](https://github.com/Nourepide/ComfyUI-Allor)
- ltdrdata [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- crystian [ComfyUI-Crystools](https://github.com/crystian/ComfyUI-Crystools)
- Fannovel16 [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)
- cubiq [ComfyUI_IPAdapter_plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus)
- spacepxl [ComfyUI-Florence-2](https://github.com/spacepxl/ComfyUI-Florence-2)
- Acly [comfyui-inpaint-nodes](https://github.com/Acly/comfyui-inpaint-nodes)
- EllangoK [ComfyUI-post-processing-nodes](https://github.com/EllangoK/ComfyUI-post-processing-nodes)
- cubiq [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)
- chflame163 [ComfyUI_LayerStyle](https://github.com/chflame163/ComfyUI_LayerStyle)
- BadCafeCode [masquerade-nodes-comfyui](https://github.com/BadCafeCode/masquerade-nodes-comfyui)
- receyuki [comfyui-prompt-reader-node](https://github.com/receyuki/comfyui-prompt-reader-node)

## Acknowledgments

I would like to thank the original authors of ComfyUI for their work and the contributors to the custom nodes for their contributions to the ComfyUI ecosystem.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
