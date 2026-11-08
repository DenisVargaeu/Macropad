# Macropad

A custom 16-key macropad with OLED display and RGB LED, built around the Raspberry Pi Pico (RP2040).

## Overview

This project is a fully open-source hardware macropad designed in KiCad 10. It features:

- **16 tactile keys** arranged in a 4×4 grid
- **0.91" OLED display** (128×32, SSD1306, I2C) for status, layer indication, or custom graphics
- **RGB LED** (5mm, common cathode) for per-key or global lighting effects
- **Raspberry Pi Pico** (RP2040) as the controller — supports both Pico and Pico 2 (RP2350)
- **Through-hole design** for easy hand soldering and assembly

## Hardware Specifications

| Component | Part | Details |
|-----------|------|---------|
| MCU | Raspberry Pi Pico / Pico 2 | RP2040 / RP2350, 133 MHz, 264 KB SRAM, 2 MB Flash |
| Display | ER_OLEDM0.91_1x-I2C | 0.91", 128×32, SSD1306, I2C (EastRising / BuyDisplay) |
| Keys | 16 × SW_PUSH_6mm | 6×6 mm tactile switches, through-hole |
| RGB LED | LED_D5.0mm-4_RGB_Wide_Pins | 5 mm, 4-pin common cathode (Kingbright WP154A4 or compatible) |
| Resistors | 3 × 1/4W axial | Current limiting for RGB LED (values TBD, typically 220–330 Ω) |
| PCB | Custom 2-layer | 1.6 mm FR4, through-hole components |

## Pinout

### Buttons (4×4 Matrix — Direct GPIO)

| Key | GPIO | Switch Ref |
|-----|------|------------|
| 1 (top-left) | GPIO0 | SW16 |
| 2 | GPIO1 | SW15 |
| 3 | GPIO2 | SW14 |
| 4 | GPIO3 | SW13 |
| 5 | GPIO4 | SW8 |
| 6 | GPIO5 | SW7 |
| 7 | GPIO6 | SW6 |
| 8 | GPIO7 | SW5 |
| 9 | GPIO8 | SW4 |
| 10 | GPIO9 | SW3 |
| 11 | GPIO10 | SW2 |
| 12 | GPIO11 | SW1 |
| 13 (bottom-left) | GPIO16 | SW9 |
| 14 | GPIO17 | SW10 |
| 15 | GPIO18 | SW11 |
| 16 (bottom-right) | GPIO19 | SW12 |

> **Note:** Each switch connects its GPIO to GND when pressed. Enable internal pull-ups in firmware.

### OLED Display (I2C)

| Signal | GPIO | Display Pin |
|--------|------|-------------|
| SCL | GPIO15 | Pin 3 (SCL) |
| SDA | GPIO14 | Pin 4 (SDA) |
| VCC | 3V3 | Pin 2 (VCC) |
| GND | GND | Pin 1 (GND) |

### RGB LED (Common Cathode)

| Color | Anode Net | Current-Limit Resistor | MCU GPIO |
|-------|-----------|------------------------|----------|
| Blue | `Net-(D2-BA)` | R1 | GPIO20 |
| Green | `Net-(D2-GA)` | R2 | GPIO21 |
| Red | `Net-(D2-RA)` | R3 | GPIO22 |
| Cathode (shared) | GND | — | — |

> **Resistor values:** Choose based on LED forward voltage and desired current (e.g., 220 Ω for ~10 mA @ 3.3 V).

## Quick View (No KiCad Required)

| Document | Link | Description |
|----------|------|-------------|
| **Schematic (PDF)** | [`macropad-schematic.pdf`](macropad-schematic.pdf) | Full schematic, all pages |
| **PCB Layout (PDF)** | [`macropad-pcb.pdf`](macropad-pcb.pdf) | All layers (Cu, Silk, Mask, Edge) |
| **3D Model (STEP)** | [`macropad-3d.step`](macropad-3d.step) | For CAD (FreeCAD, Fusion 360, OnShape) |
| **3D Model (STL, Full)** | [`macropad-3d-full.stl`](macropad-3d-full.stl) | **All components** (18 MB) — PCB, Pico, 16 keys, LED, resistors, OLED |
| **3D Model (STL, PCB+Pico)** | [`macropad-pcb-pico.stl`](macropad-pcb-pico.stl) | Board + Pico only (6 MB) — for enclosure design |
| **3D Model (STL, Buttons only)** | [`macropad-3d.stl`](macropad-3d.stl) | Original export (buttons only, 0.4 MB) |

## Repository Structure

```
macropad/
├── macropad.kicad_pro           # KiCad project file
├── macropad.kicad_sch           # Schematic
├── macropad.kicad_pcb           # PCB layout
├── macropad-schematic.pdf       # Exported schematic (PDF)
├── macropad-pcb.pdf             # Exported PCB layers (PDF)
├── macropad-3d.step             # 3D model (STEP) — for CAD
├── macropad-3d-full.stl         # 3D model (STL) — ALL components (18 MB)
├── macropad-pcb-pico.stl        # 3D model (STL) — PCB + Pico only (6 MB)
├── macropad-3d.stl              # 3D model (STL) — buttons only (0.4 MB)
├── export_stl.py                # FreeCAD script used for STL export
├── gerbers/                     # Gerber files for fabrication (generated)
├── LICENSE                      # CERN-OHL-P-2.0 license
└── README.md                    # This file
```

## Getting Started

### Prerequisites

- **KiCad 10.0** or later ([download](https://www.kicad.org/download/))
- Raspberry Pi Pico SDK (for firmware development)
- Soldering equipment (through-hole components)

### Opening the Project

1. Clone this repository
2. Open `macropad.kicad_pro` in KiCad
3. The schematic (`macropad.kicad_sch`) and PCB (`macropad.kicad_pcb`) will load automatically

### Fabrication

1. Generate Gerbers: `File → Fabrication Outputs → Gerbers (.gbr)`
2. Generate Drill files: `File → Fabrication Outputs → Drill Files (.drl)`
3. Send to your preferred PCB manufacturer (JLCPCB, PCBWay, OSH Park, etc.)

**Board specs for fabrication:**
- 2 layers
- 1.6 mm thickness
- Standard FR4
- Minimum track/space: 0.15 mm (6 mil) — adjust per fab house rules
- Through-hole pads for all components

### Assembly

All components are through-hole except the Pico module (which uses castellated pads). Recommended assembly order:

1. Solder resistors (R1, R2, R3)
2. Solder tactile switches (SW1–SW16)
3. Solder RGB LED (D2) — note orientation (pin 1 = Blue anode, marked on silkscreen)
4. Solder OLED display (U1) — pin 1 is GND (square pad)
5. Solder female headers for Pico module (or socket Pico directly)
6. Insert Pico module

## Firmware

This repository contains **hardware only**. Firmware is not included but can be developed using:

- **C/C++** with [Pico SDK](https://github.com/raspberrypi/pico-sdk)
- **CircuitPython** — copy `.uf2` to Pico in BOOTSEL mode
- **MicroPython** — similar to CircuitPython
- **KMK** — Python-based keyboard firmware
- **QMK** — C-based keyboard firmware (Pico support via RP2040 port)

### Minimal Firmware Example (CircuitPython)

```python
import board
import digitalio
import busio
import adafruit_ssd1306
import neopixel

# Buttons (with pull-ups)
keys = [digitalio.DigitalInOut(getattr(board, f"GP{i}")) for i in range(12)] + \
       [digitalio.DigitalInOut(getattr(board, f"GP{i}")) for i in range(16, 20)]
for k in keys:
    k.direction = digitalio.Direction.INPUT
    k.pull = digitalio.Pull.UP

# I2C for OLED
i2c = busio.I2C(board.GP15, board.GP14)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# RGB LED
led = neopixel.NeoPixel(board.GP20, 1)  # Use GP20/21/22 with PWM for RGB
# Note: Requires PWM on all three channels for color mixing
```

## Customization

- **Key layout:** Modify switch positions in `macropad.kicad_pcb`
- **Display:** Footprint supports ER_OLEDM0.91_1x-I2C; swap for other I2C OLEDs by changing footprint
- **LED:** Use different RGB LED by updating `LED_THT:LED_D5.0mm-4_RGB_Wide_Pins` footprint
- **MCU:** Footprint `Module:RaspberryPi_Pico_Common_Unspecified` supports Pico, Pico W, and Pico 2

## License

This hardware design is released under the **CERN Open Hardware Licence Version 2 - Permissive (CERN-OHL-P-2.0)**.

```
Copyright (c) 2026 Denis Varga

Licensed under the CERN-OHL-P-2.0 or any later version.
You may redistribute and modify this design under the terms of the CERN-OHL-P-2.0.
This design is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY.
See the CERN-OHL-P-2.0 for details.
```

SPDX-License-Identifier: CERN-OHL-P-2.0

## Contributing

Pull requests welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes in KiCad 10+
4. Run DRC (`Inspect → Design Rules Checker`) before committing
5. Submit a PR with a clear description

## Resources

- [Raspberry Pi Pico Datasheet](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)
- [SSD1306 OLED Datasheet (ER-OLEDM0.91-1)](https://www.buydisplay.com/download/manual/ER-OLEDM0.91-1_Datasheet.pdf)
- [Kingbright WP154A4 RGB LED Datasheet](https://www.kingbright.com/attachments/file/psearch/000/00/00/L-154A4SUREQBFZGEW(Ver.11A).pdf)
- [KiCad Documentation](https://docs.kicad.org/)

---

**Designed with KiCad 10.0** • Made for makers, by makers