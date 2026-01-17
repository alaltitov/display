# About

This project provides ESPHome firmware for the 4848S040 display board, featuring an ESP32-S3 microcontroller with integrated display capabilities.

## Features

- **ESP32-S3 Based**: Powered by the ESP32-S3 with ESP-IDF framework
- **Easy Setup**: Simple Wi-Fi provisioning via Bluetooth LE or captive portal
- **OTA Updates**: Over-the-air firmware updates for seamless maintenance
- **ESPHome Integration**: Full integration with Home Assistant via ESPHome dashboard
- **Web-based Installation**: No tools required - install directly from your browser using USB

## Getting Started

1. Connect your device to your computer via USB
2. Click the install button below
3. Follow the on-screen instructions to flash the firmware
4. Configure Wi-Fi using the captive portal or Bluetooth LE provisioning
5. Add the device to your Home Assistant instance

## Installation

You can use the button below to install the pre-built firmware directly to your device via USB from the browser.

<esp-web-install-button manifest="firmware/display01.manifest.json"></esp-web-install-button>

<script type="module" src="https://unpkg.com/esp-web-tools@10/dist/web/install-button.js?module"></script>
