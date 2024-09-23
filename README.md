# ComfyUI_Limited: A Lightweight Alternative

Get started with ComfyUI Limited, a stripped-down alternative to run your [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that meets the minimum requirements for a quick and lightweight graph interface experience. Just like a workflow viewer.

## Why Limited Mode?

Limited Mode is a lightweight alternative to ComfyUI, created to provide an alternative method to run your ComfyUI. It's ideal for situations where you need to quickly access the graph interface without the overhead of the full ComfyUI.
That said, this can be a demo capable of loading workflows with custom nodes and without the installation of requirements that is fast to restart, sort of workflow viewer.
You can modify the script to suit your needs, like letting certain modules to load for dev purposes.

## Features

- Lightweight: ComfyUI Limited requires minimal resources, making it suitable for testing and development environments.
- Fast: Load the graph interface quickly, without the overhead of the full ComfyUI.
- Utilizes common practices: ComfyUI Limited uses test-driven development practices to ensure compatibility with your existing ComfyUI setup.

## Limitations**

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

2. Install the required packages:
    ```sh
    pip install aiohttp
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

• ComfyUI Limited is intended for graphical user interface use only, so you won't be able to generate images.
• Currently, ComfyUI Limited only supports 5 custom nodes. If you have more installed, they will load, but may not function as expected.
• Keep in mind that ComfyUI Limited is a stripped-down instance of ComfyUI, and all features not related to graph nodes will not be available.

## Acknowledgments

I would like to thank the original authors of ComfyUI for their work and the contributors to the custom nodes for their contributions to the ComfyUI ecosystem.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
