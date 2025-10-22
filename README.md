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
 <img width="200px" src="/doc/images/media_player.png">
</p>

<p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/made%20by-alaltitov-blue">
    <img alt="Static Badge" src="https://img.shields.io/badge/version-v1.0%20Dev-green">
    <img alt="Static Badge" src="https://img.shields.io/badge/esphome test version-2025.9.3-red">
    <img alt="Static Badge" src="https://img.shields.io/badge/license-MIT-orange">
</p>

## Support the Project

<img src="/doc/images/donate.png" alt="QR Code" width="150" align="left" hspace="10"/>

<b>Support me on</b><br/>
<a href="https://boosty.to/altitov/donate">
  <img src="/doc/images/boosty.png" alt="Boosty" width="120"/>
</a>

<br clear="all"/>

## ⚠️ Important Notice
- Support for new versions will be provided only for the release version (while the dev branch is in effect) 
- Beta and alpha versions will not be supported taking into account new versions of ESPHome.

## ✨ Features

- Status indicators for Wi-Fi, Home Assistant API, thermostat, air conditioner, touchscreen lock, alarm panel
- Weather icons with current conditions and temperature
- Weather Forecasts daily and hourly
- Date and time
- Sensor readings from Home Assistant
- Climate control (auto)
- Lights control (auto)
- Media player
- Other controls (for example, vacuum, alarm panel, shutter, fan, switchs...) coming soon
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
    - it (from [echopage1964](https://github.com/echopage1964))

## 📦 Installation
> 📹 **Video [instruction](https://youtu.be/HYN_2hvcbes?si=JfYQH4vCuFlr8Q9r)**

<img width="400px" src="/doc/images/ha_options.png">

- You must enable the "Allow the device to perform Home Assistant actions." option in the ESPHome integration to Home Assistant to control devices.
- Install custom component for forecasts and covers for media player from [here](https://github.com/alaltitov/homeassistant-display-tools).
- Copy repository to vscode or to esphome folder of your Home Assistant. Change in substitutions.yaml and config.yaml (light folder) your entities in all widgets (only in substitution, in code everything will be substituted automatically).

## 📖 Documentation
- [Firmware](https://alaltitov.github.io/Guition-ESP32-S3-4848S040-DOCS)  (Need update, coming soon...)
- [ESPHome LVGL 8.4](https://esphome.io/components/lvgl/)

## 🤝 Thanks for your help

- Thanks, [сlydebarrow](https://github.com/clydebarrow), [jesserockz](https://github.com/jesserockz), [ssieb](https://github.com/ssieb) for helping me with the project!
