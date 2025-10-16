# LVGL ESPhome Guition ESP32-S3-4848S040 custom firmware

<p align="center">
 <img width="200px" src="/doc/images/loading.png">
 <img width="200px" src="/doc/images/home.png">
 <img width="200px" src="/doc/images/forecasts.png">
 <img width="200px" src="/doc/images/info.png">
 <img width="200px" src="/doc/images/settings.png">
 <img width="200px" src="/doc/images/light0.png">
 <img width="200px" src="/doc/images/light1.png">
 <img width="200px" src="/doc/images/climate0.png">
 <img width="200px" src="/doc/images/climate1.png">
 <img width="200px" src="/doc/images/climate2.png">
 <img width="200px" src="/doc/images/climate3.png">
</p>

<p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/made%20by-alaltitov-blue">
    <img alt="Static Badge" src="https://img.shields.io/badge/version-v1.0%20Dev-green">
    <img alt="Static Badge" src="https://img.shields.io/badge/esphome test version-2025.9.3-red">
    <img alt="Static Badge" src="https://img.shields.io/badge/license-MIT-orange">
</p>

## ✨ Features

- Status indicators for Wi-Fi, Home Assistant API, thermostat, air conditioner, touchscreen lock, alarm panel
- Weather icons with current conditions and temperature
- Weather Forecasts daily and hourly
- Date and time
- Sensor readings from Home Assistant
- Climate control (auto)
- lights control (auto)
- Other controls (for example, vacuum, alarm panel, shutter, fan, media player, switchs...) coming soon
- Settings:
  * Backlight adjustment
  * Screen timeout settings
  * Language selection:
    - ru (from [alaltitov](https://github.com/alaltitov))
    - en (from [alaltitov](https://github.com/alaltitov))
    - pl (from [reaper7](https://github.com/reaper7))
    - fr (from [lboue](https://github.com/lboue))
    - es (from Antonio)
    - nl (from [zjean](https://github.com/zjean))
    - si (from [Protoncek](https://github.com/Protoncek))

## 📦 Installation
> 📹 **Video [instruction](https://youtu.be/HYN_2hvcbes?si=JfYQH4vCuFlr8Q9r)**

<img width="400px" src="/doc/images/ha_options.png">

- You must enable the "Allow the device to perform Home Assistant actions." option in the ESPHome integration to Home Assistant to control devices.
- Install custom component for forecasts and covers for media player from [here](https://github.com/alaltitov/homeassistant-display-tools).
- Copy repository to vscode or to esphome folder of your Home Assistant. Change in substitutions.yaml and config.yaml (light folder) your entities in all widgets (only in substitution, in code everything will be substituted automatically).

## ⚠️ Important Notice
- Support for new versions will be provided only for the release version (while the dev branch is in effect); beta and alpha versions will not be supported taking into account new versions of ESPHome.

## 📖 Documentation
- [Firmware](https://alaltitov.github.io/Guition-ESP32-S3-4848S040-DOCS) - Need update. Coming soon.
- [ESPHome LVGL 8.4](https://esphome.io/components/lvgl/)

## 🤝 Thanks for your help

- Thanks, [сlydebarrow](https://github.com/clydebarrow), [jesserockz](https://github.com/jesserockz), [ssieb](https://github.com/ssieb) for helping me with the project!

## 💝 Support the Project
This project was made in my free time and if it was useful to you, you can support me if you find it necessary 😊:

**ETH/USDT (ERC-20):** `0x9fF0E16a58229bEcdFDf47d9759f20bE77356994`

Or just put ⭐ Thank you
