# Macropad

<p align="center">
  <a href="https://github.com/DenisVargaeu/Macropad/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-CERN--OHL--P--2.0-blue.svg" alt="License"></a>
  <a href="https://www.kicad.org/"><img src="https://img.shields.io/badge/Designed%20in-KiCad%2010.0-green.svg" alt="KiCad 10"></a>
  <a href="https://github.com/DenisVargaeu/Macropad/releases"><img src="https://img.shields.io/github/v/release/DenisVargaeu/Macropad?include_prereleases" alt="Release"></a>
  <a href="https://github.com/DenisVargaeu/Macropad/issues"><img src="https://img.shields.io/github/issues/DenisVargaeu/Macropad" alt="Issues"></a>
</p>

<p align="center">
  <strong>A custom 16-key macropad with OLED display and RGB LED, built around the Raspberry Pi Pico (RP2040/RP2350).</strong>
</p>

<p align="center">
  <a href="#-quick-view">Quick View</a> •
  <a href="#-features">Features</a> •
  <a href="#-hardware-specifications">Specs</a> •
  <a href="#-pinout">Pinout</a> •
  <a href="#-repository-structure">Repository</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-bill-of-materials">BOM</a> •
  <a href="#-firmware">Firmware</a> •
  <a href="#-fabrication">Fabrication</a> •
  <a href="#-assembly">Assembly</a> •
  <a href="#-customization">Customization</a> •
  <a href="#-license">License</a>
</p>

---

## 📸 Quick View

| Document | Preview | Description |
|----------|---------|-------------|
| **Schematic** | [![Schematic](https://img.shields.io/badge/PDF-macropad--schematic.pdf-red?logo=adobe-acrobat-reader)](macropad-schematic.pdf) | Full schematic, all pages |
| **PCB Layout** | [![PCB](https://img.shields.io/badge/PDF-macropad--pcb.pdf-green?logo=adobe-acrobat-reader)](macropad-pcb.pdf) | All layers (Cu, Silk, Mask, Edge) |
| **3D Model (STEP)** | [![STEP](https://img.shields.io/badge/STEP-macropad--3d.step-orange?logo=freecad)](macropad-3d.step) | For CAD (FreeCAD, Fusion 360, OnShape) |
| **3D Model (STL — Full)** | [![STL](https://img.shields.io/badge/STL-macropad--3d--full.stl-purple?logo=prusa)](macropad-3d-full.stl) | **All components** (18 MB) |
| **3D Model (STL — PCB+Pico)** | [![STL](https://img.shields.io/badge/STL-macropad--pcb--pico.stl-purple?logo=prusa)](macropad-pcb-pico.stl) | Board + Pico only (6 MB) — for enclosures |
| **3D Model (STL — Buttons only)** | [![STL](https://img.shields.io/badge/STL-macropad--3d.stl-purple?logo=prusa)](macropad-3d.stl) | Buttons only (0.4 MB) |

> 💡 **View in browser:** Click any PDF/STL link above — GitHub renders them natively. No KiCad required!

---

## ✨ Features

- **16 tactile keys** in a 4×4 matrix — direct GPIO (no matrix scanning needed)
- **0.91″ OLED display** (128×32, SSD1306, I2C) — status, layers, animations
- **RGB LED** (5 mm, common cathode) — per-key or global lighting
- **Raspberry Pi Pico / Pico 2** — RP2040 or RP2350, USB-C, BOOTSEL button accessible
- **Through-hole only** — easy hand soldering, beginner-friendly
- **Open hardware** — CERN-OHL-P-2.0 license, modify freely

---

## 🔧 Hardware Specifications

| Component | Part | Qty | Details |
|-----------|------|-----|---------|
| **MCU** | Raspberry Pi Pico / Pico 2 | 1 | RP2040 / RP2350, 133 MHz, 264 KB SRAM, 2 MB Flash |
| **Display** | ER_OLEDM0.91_1x-I2C | 1 | 0.91″, 128×32, SSD1306, I2C (EastRising/BuyDisplay) |
| **Keys** | SW_PUSH_6mm (6×6 mm tactile) | 16 | Through-hole, 4-pin (2×2 internally connected) |
| **RGB LED** | LED_D5.0mm-4_RGB_Wide_Pins | 1 | 5 mm, 4-pin common cathode (Kingbright WP154A4) |
| **Resistors** | 1/4 W axial (220–330 Ω) | 3 | Current limiting for R/G/B channels |
| **PCB** | Custom 2-layer | 1 | 1.6 mm FR4, ENIG/HASL, 100×60 mm approx. |

---

## 📌 Pinout

### Buttons — Direct GPIO (4×4 Grid)

| Key | Position | GPIO | Switch Ref | Net Name |
|-----|----------|------|------------|----------|
| 1 | Top-Left | GPIO0 | SW16 | `Net-(A1-GPIO0)` |
| 2 | | GPIO1 | SW15 | `Net-(A1-GPIO1)` |
| 3 | | GPIO2 | SW14 | `Net-(A1-GPIO2)` |
| 4 | Top-Right | GPIO3 | SW13 | `Net-(A1-GPIO3)` |
| 5 | | GPIO4 | SW8 | `Net-(A1-GPIO4)` |
| 6 | | GPIO5 | SW7 | `Net-(A1-GPIO5)` |
| 7 | | GPIO6 | SW6 | `Net-(A1-GPIO6)` |
| 8 | | GPIO7 | SW5 | `Net-(A1-GPIO7)` |
| 9 | | GPIO8 | SW4 | `Net-(A1-GPIO8)` |
| 10 | | GPIO9 | SW3 | `Net-(A1-GPIO9)` |
| 11 | | GPIO10 | SW2 | `Net-(A1-GPIO10)` |
| 12 | | GPIO11 | SW1 | `Net-(A1-GPIO11)` |
| 13 | Bottom-Left | GPIO16 | SW9 | `Net-(A1-GPIO16)` |
| 14 | | GPIO17 | SW10 | `Net-(A1-GPIO17)` |
| 15 | | GPIO18 | SW11 | `Net-(A1-GPIO18)` |
| 16 | Bottom-Right | GPIO19 | SW12 | `Net-(A1-GPIO19)` |

> **Each switch:** GPIO → GND when pressed. **Enable internal pull-ups** in firmware (`Pin.PULL_UP`).

### OLED Display (I2C)

| Signal | GPIO | Display Pin | Net |
|--------|------|-------------|-----|
| SCL | GPIO15 | Pin 3 | `Net-(A1-GPIO15)` |
| SDA | GPIO14 | Pin 4 | `Net-(A1-GPIO14)` |
| VCC | 3V3 | Pin 2 | `VCC` |
| GND | GND | Pin 1 | `GND` |

### RGB LED (Common Cathode)

| Color | Anode Net | Resistor | MCU GPIO |
|-------|-----------|----------|----------|
| **Blue** | `Net-(D2-BA)` | R1 | GPIO20 |
| **Green** | `Net-(D2-GA)` | R2 | GPIO21 |
| **Red** | `Net-(D2-RA)` | R3 | GPIO22 |
| **Cathode** | GND | — | — |

> **Resistor values:** 220 Ω (≈10 mA @ 3.3 V) or 330 Ω (≈7 mA). Adjust for brightness/uniformity.

---

## 📁 Repository Structure

```
macropad/
├── 📋 KiCad Source (editable)
│   ├── macropad.kicad_pro          # Project file
│   ├── macropad.kicad_sch          # Schematic
│   ├── macropad.kicad_pcb          # PCB layout
│   └── macropad.kicad_prl          # Local settings
│
├── 📄 Documentation (view anywhere)
│   ├── macropad-schematic.pdf      # Full schematic (PDF)
│   └── macropad-pcb.pdf            # PCB all layers (PDF)
│
├── 🎯 3D Models
│   ├── macropad-3d.step            # STEP — for CAD (FreeCAD, Fusion 360)
│   ├── macropad-3d-full.stl        # STL — ALL components (18 MB)
│   ├── macropad-pcb-pico.stl       # STL — PCB + Pico only (6 MB)
│   └── macropad-3d.stl             # STL — buttons only (0.4 MB)
│
├── 🏭 Fabrication
│   └── gerbers/                    # Gerber + drill files (gitignored)
│
├── 🔧 Utilities
│   └── export_stl.py               # FreeCAD script for STL export
│
├── 📜 LICENSE                      # CERN-OHL-P-2.0
└── 📖 README.md                    # This file
```

### Files by Category

| Category | Files | Purpose |
|----------|-------|---------|
| **KiCad Source** | `.kicad_pro`, `.kicad_sch`, `.kicad_pcb`, `.kicad_prl` | Full editable design — open in KiCad 10+ |
| **Documentation** | `macropad-schematic.pdf`, `macropad-pcb.pdf` | View schematic/PCB without KiCad |
| **3D Models** | `.step`, `.stl` (3 variants) | CAD, 3D printing, enclosure design |
| **Fabrication** | `gerbers/` (generated) | Send to PCB manufacturer |
| **License** | `LICENSE` | CERN-OHL-P-2.0 (permissive open hardware) |

---

## 🚀 Getting Started

### Prerequisites

- **KiCad 10.0+** — [Download](https://www.kicad.org/download/)
- **Raspberry Pi Pico SDK** — for C/C++ firmware
- **Soldering iron, solder, flux** — through-hole components
- **Female headers (2×20)** — for Pico module (or solder directly)

### Opening the Project

```bash
git clone https://github.com/DenisVargaeu/Macropad.git
cd Macropad
# Open in KiCad
open macropad.kicad_pro    # macOS
xdg-open macropad.kicad_pro  # Linux
start macropad.kicad_pro     # Windows
```

> **All KiCad source files are included.** No need to re-create anything — just open and edit.

---

## 📦 Bill of Materials (BOM)

| Qty | Ref | Part | Value / Spec | Notes |
|-----|-----|------|--------------|-------|
| 1 | A1 | Raspberry Pi Pico / Pico 2 | RP2040 / RP2350 | With headers or castellated |
| 1 | U1 | ER_OLEDM0.91_1x-I2C | 128×32, SSD1306, I2C | EastRising / BuyDisplay |
| 16 | SW1–SW16 | Tactile switch 6×6 mm | SW_PUSH_6mm | 4-pin, through-hole |
| 1 | D2 | RGB LED 5 mm | Common cathode, 4-pin | Kingbright WP154A4 or compatible |
| 3 | R1, R2, R3 | Resistor 1/4 W axial | 220–330 Ω | Current limiting (R/G/B) |
| 1 | — | PCB | Custom, 2-layer | Order from Gerbers |

**Approximate cost (per unit, qty 1):** ~$15–25 USD (Pico + display + switches + PCB)

---

## 🏭 Fabrication

### Option A: Use Pre-generated Gerbers (Recommended)

The `gerbers/` directory contains production-ready files:

```
gerbers/
├── macropad-F_Cu.gtl        # Front copper
├── macropad-B_Cu.gbl        # Back copper
├── macropad-F_Silkscreen.gto # Front silkscreen
├── macropad-B_Silkscreen.gbo # Back silkscreen
├── macropad-F_Mask.gts       # Front soldermask
├── macropad-B_Mask.gbs       # Back soldermask
├── macropad-Edge_Cuts.gm1    # Board outline
└── macropad.drl              # Drill file
```

Upload to **JLCPCB, PCBWay, OSH Park, AISLER**, etc.

### Option B: Generate from KiCad

1. Open `macropad.kicad_pro` in KiCad
2. `File → Fabrication Outputs → Gerbers (.gbr)`
   - Layers: F.Cu, B.Cu, F.SilkS, B.SilkS, F.Mask, B.Mask, Edge.Cuts
   - Format: Gerber X2, mm, 4.6
3. `File → Fabrication Outputs → Drill Files (.drl)`
   - Format: Excellon, mm, PTH+NPTH
4. Zip and send to fab

### Board Specifications

| Parameter | Value |
|-----------|-------|
| Layers | 2 |
| Thickness | 1.6 mm |
| Material | FR4 (standard) |
| Copper weight | 1 oz (35 µm) |
| Min track/space | 0.15 mm / 0.15 mm (6/6 mil) |
| Min drill | 0.3 mm (12 mil) |
| Surface finish | HASL or ENIG |
| Soldermask | Green (standard) |
| Silkscreen | White |

---

## 🔨 Assembly

### Component Placement

All components are **through-hole** except the Pico (castellated pads).

### Recommended Soldering Order

| Step | Components | Tips |
|------|------------|------|
| 1 | **Resistors** (R1, R2, R3) | Lowest profile first |
| 2 | **Tactile switches** (SW1–SW16) | Snap in, solder one pin, align, solder rest |
| 3 | **RGB LED** (D2) | Pin 1 = Blue anode (square pad on silkscreen) |
| 4 | **OLED display** (U1) | Pin 1 = GND (square pad); use socket if desired |
| 5 | **Female headers** for Pico | 2×20 pin, 2.54 mm pitch |
| 6 | **Insert Pico module** | Align USB-C with board cutout |

### Orientation Notes

- **Switches:** 4 pins, internally connected in pairs — orientation doesn't matter electrically
- **RGB LED:** Pin 1 (Blue) marked on silkscreen; cathode is longest pin
- **OLED:** Pin 1 = GND (square pad on footprint)
- **Pico:** USB-C faces board edge; BOOTSEL button accessible

---

## 💻 Firmware

This repository contains **hardware only**. Firmware examples below.

### Supported Frameworks

| Framework | Language | Status | Link |
|-----------|----------|--------|------|
| **Pico SDK** | C/C++ | ✅ Native | [pico-sdk](https://github.com/raspberrypi/pico-sdk) |
| **CircuitPython** | Python | ✅ Easy | [circuitpython.org](https://circuitpython.org/board/raspberry_pi_pico/) |
| **MicroPython** | Python | ✅ Official | [micropython.org](https://micropython.org/download/rp2-pico/) |
| **KMK** | Python | ✅ Keyboard-focused | [kmkfw.io](https://kmkfw.io/) |
| **QMK** | C | ✅ Community port | [qmk.fm](https://qmk.fm/) |
| **ZMK** | C/Zephyr | ⚠️ Advanced | [zmk.dev](https://zmk.dev/) |

### Minimal CircuitPython Example

```python
# macropad_firmware.py — copy to CIRCUITPY drive
import board
import digitalio
import busio
import adafruit_ssd1306
import neopixel

# ── Buttons (16 direct GPIOs with pull-ups) ──────────────────────
key_pins = [getattr(board, f"GP{i}") for i in list(range(12)) + list(range(16, 20))]
keys = [digitalio.DigitalInOut(pin) for pin in key_pins]
for k in keys:
    k.direction = digitalio.Direction.INPUT
    k.pull = digitalio.Pull.UP

# ── OLED (I2C on GP14/GP15) ──────────────────────────────────────
i2c = busio.I2C(board.GP15, board.GP14)
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
display.fill(0)
display.text("Macropad Ready", 0, 0, 1)
display.show()

# ── RGB LED (PWM on GP20/21/22) ─────────────────────────────────
# Note: Requires 3 PWM channels for color mixing
import pwmio
red_pwm = pwmio.PWMOut(board.GP22, frequency=1000, duty_cycle=0)
grn_pwm = pwmio.PWMOut(board.GP21, frequency=1000, duty_cycle=0)
blu_pwm = pwmio.PWMOut(board.GP20, frequency=1000, duty_cycle=0)

def set_color(r, g, b):
    red_pwm.duty_cycle = int(r * 65535)
    grn_pwm.duty_cycle = int(g * 65535)
    blu_pwm.duty_cycle = int(b * 65535)

# ── Main loop ─────────────────────────────────────────────────────
while True:
    for i, k in enumerate(keys):
        if not k.value:  # Pressed (active low)
            print(f"Key {i+1} pressed")
            set_color(1, 0, 0)  # Red on press
        else:
            set_color(0, 0, 0)  # Off
```

### Pico SDK (C) — Button Scan Skeleton

```c
// main.c
#include "pico/stdlib.h"
#include "hardware/i2c.h"
#include "hardware/pwm.h"

#define I2C_PORT i2c1
#define SDA_PIN 14
#define SCL_PIN 15

// Button GPIOs in order
const uint btn_gpios[] = {0,1,2,3,4,5,6,7,8,9,10,11,16,17,18,19};
const uint NUM_BTNS = 16;

// RGB PWM pins
const uint RED_PIN = 22, GRN_PIN = 21, BLU_PIN = 20;

int main() {
    stdio_init_all();

    // Buttons with pull-ups
    for (int i = 0; i < NUM_BTNS; i++) {
        gpio_init(btn_gpios[i]);
        gpio_set_dir(btn_gpios[i], GPIO_IN);
        gpio_pull_up(btn_gpios[i]);
    }

    // I2C for OLED
    i2c_init(I2C_PORT, 400000);
    gpio_set_function(SDA_PIN, GPIO_FUNC_I2C);
    gpio_set_function(SCL_PIN, GPIO_FUNC_I2C);
    gpio_pull_up(SDA_PIN); gpio_pull_up(SCL_PIN);

    // PWM for RGB
    for (uint pin : {RED_PIN, GRN_PIN, BLU_PIN}) {
        gpio_set_function(pin, GPIO_FUNC_PWM);
        uint slice = pwm_gpio_to_slice_num(pin);
        pwm_set_wrap(slice, 255);
        pwm_set_enabled(slice, true);
    }

    while (true) {
        for (int i = 0; i < NUM_BTNS; i++) {
            if (!gpio_get(btn_gpios[i])) {
                printf("Key %d pressed\n", i+1);
                pwm_set_gpio_level(RED_PIN, 255);
            } else {
                pwm_set_gpio_level(RED_PIN, 0);
            }
        }
        sleep_ms(10);
    }
}
```

### KMK (Python Keyboard Firmware)

```python
# kmk_config.py
import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()

# Direct pin matrix (no diodes needed with pull-ups)
keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3,
    board.GP4, board.GP5, board.GP6, board.GP7,
    board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP16, board.GP17, board.GP18, board.GP19,
)
keyboard.row_pins = (board.GND,)  # Single row to GND
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB on GP20/21/22
rgb = RGB(pixel_pin=board.GP20, num_pixels=1, val_default=50)
keyboard.modules.append(rgb)

# Keymap
keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4,
     KC.N5, KC.N6, KC.N7, KC.N8,
     KC.N9, KC.A, KC.B, KC.C,
     KC.D, KC.E, KC.F, KC.G]
]

if __name__ == '__main__':
    keyboard.go()
```

---

## 🎨 Customization

| Change | How |
|--------|-----|
| **Key layout** | Edit switch positions in `macropad.kicad_pcb` (Footprint Properties → Position) |
| **Display** | Replace `Display:ER_OLEDM0.91_1x-I2C` footprint with any I2C OLED (SSD1306, SH1106) |
| **RGB LED** | Swap `LED_THT:LED_D5.0mm-4_RGB_Wide_Pins` for common-anode or different package |
| **MCU** | Footprint `Module:RaspberryPi_Pico_Common_Unspecified` supports Pico, Pico W, Pico 2 |
| **Add per-key LEDs** | Add 16× SK6812MINI-E or WS2812B footprints + series resistors |
| **Rotary encoder** | Add EC11 footprint + 2 GPIOs (e.g., GP26/GP27) |

---

## 🐛 Known Issues / Errata

| Issue | Status | Workaround |
|-------|--------|------------|
| OLED 3D model missing in KiCad library | ⚠️ Known | STL/STEP exports show placeholder; download model from BuyDisplay |
| Pico USB-C cutout may need filing | ⚠️ Minor | Test fit before soldering headers |
| RGB LED pins tight for 5 mm wide-pin | ⚠️ Minor | Slightly bend leads or use standard 2.54 mm spacing LED |

---

## 📝 Changelog

| Version | Date | Changes |
|---------|------|---------|
| **v1.0.0** | 2026-11-08 | Initial release — schematic, PCB, 3D models, documentation |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-idea`
3. Make changes in **KiCad 10+**
4. Run DRC: `Inspect → Design Rules Checker` (must pass with 0 errors)
5. Update README if needed
6. Submit PR with clear description and screenshots

### Development Setup

```bash
# Install KiCad 10+ (Ubuntu/Debian)
sudo add-apt-repository ppa:kicad/kicad-10.0-releases
sudo apt update && sudo apt install kicad

# Or download from kicad.org
```

---

## 📚 Resources

- **Raspberry Pi Pico Datasheet** — <https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf>
- **Pico 2 (RP2350) Datasheet** — <https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf>
- **SSD1306 OLED (ER-OLEDM0.91-1)** — <https://www.buydisplay.com/download/manual/ER-OLEDM0.91-1_Datasheet.pdf>
- **Kingbright WP154A4 RGB LED** — <https://www.kingbright.com/attachments/file/psearch/000/00/00/L-154A4SUREQBFZGEW(Ver.11A).pdf>
- **KiCad 10 Documentation** — <https://docs.kicad.org/10.0/>
- **Pico SDK** — <https://github.com/raspberrypi/pico-sdk>
- **CircuitPython for Pico** — <https://circuitpython.org/board/raspberry_pi_pico/>

---

## ⚖️ License

This hardware design is released under the **CERN Open Hardware Licence Version 2 - Permissive (CERN-OHL-P-2.0)**.

```
Copyright (c) 2026 Denis Varga

Licensed under the CERN-OHL-P-2.0 or any later version.
You may redistribute and modify this design under the terms of the CERN-OHL-P-2.0.
This design is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY.
See the CERN-OHL-P-2.0 for details.
```

**SPDX-License-Identifier:** `CERN-OHL-P-2.0`

Full license text: <https://ohwr.org/cern_ohl_p_2_0.txt> | <https://opensource.org/licenses/CERN-OHL-P-2.0>

---

<p align="center">
  <strong>Designed with ❤️ in KiCad 10.0</strong><br>
  Made for makers, by makers
</p>

<p align="center">
  <a href="https://github.com/DenisVargaeu/Macropad">⭐ Star this repo</a> •
  <a href="https://github.com/DenisVargaeu/Macropad/issues">🐛 Report bug</a> •
  <a href="https://github.com/DenisVargaeu/Macropad/discussions">💬 Discuss</a>
</p>