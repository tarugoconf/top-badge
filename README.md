# TOP & Badger 2040(W) <!-- omit in toc -->

An eink badge project for [top.gal](https://top.gal) events using the Badger 2040(W) board.

> ⚠️ **Work In Progress** ⚠️
>
> This project is under development and still far from being finished. But don't let that stop you from taking a look at the code and contributing to it :)

## Table of Contents <!-- omit in toc -->

- [Setup](#setup)
  - [Upgrade firmware](#upgrade-firmware)
  - [Install VSCode recommended extensions](#install-vscode-recommended-extensions)
  - [Create a python virtual environment and activate it](#create-a-python-virtual-environment-and-activate-it)
  - [Install dependencies in your virtual environment](#install-dependencies-in-your-virtual-environment)
  - [Setup MicroPico Project](#setup-micropico-project)
  - [Generate QR code matrix](#generate-qr-code-matrix)
- [References](#references)
- [License](#license)
- [Contributing](#contributing)

## Setup

### Upgrade firmware

First of all, update the firmware on your Badger 2040(W) to the latest version.

Just follow the instructions in the [Pimoroni Badger 2040W](https://github.com/pimoroni/badger2040) repository.

### Install VSCode recommended extensions

Use whatever IDE you want (as long as it supports Micropython), but we recommend using VSCode with the following extensions installed:

```json
{
    "recommendations": [
        "ms-python.python",
        "visualstudioexptteam.vscodeintellicode",
        "ms-python.vscode-pylance",
        "paulober.pico-w-go"
    ]
}
```

### Create a python virtual environment and activate it

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies in your virtual environment

```bash
pip3 install -r requirements.txt
```

### Setup MicroPico Project

From the VSCode command palette, run: "MicroPico: Setup MicroPico project".

IT will create a `.micropico` file in the root of the project to identify it.

If everything is set up correctly, yoy can now select a `MicroPico vREPL` terminal in VSCode, and if there's no issue connecting to the badge you will see something similar to this:

```bash
MicroPython v1.23.0-dirty on 2024-06-21; Pimoroni Badger2040W 2MB with RP2040
Type "help()" for more information or .help for custom vREPL commands.

>>> 
```

### Generate QR code matrix

To generate the QR code matrix:

1. Edit the `DATA` variable in `src/assets/qr/qrcode_URL_generator.py` to contain the URL or text to encode.
2. Run the script:

```bash
python3 src/assets/qr/qrcode_URL_generator.py
```

It should automatically generate the `src/assets/qr/bit_matrix.py` file with the QR code matrix that is imported in the `main.py` file as `BIT_MATRIX`.

## References

- [Badger 2040 & Badger 2040 W - repository](https://github.com/pimoroni/badger2040)
- [Pico Graphics library - repository](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/picographics)

## License

The badge holder is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](./badge-holder/LICENSE_CC-BY-NC.txt).

All the code is licensed under the [MIT License](LICENSE).

## Contributing

To join the repository as a contributor, please see [CONTRIBUTING.md](CONTRIBUTING.md).
