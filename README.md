# LVGL ESPhome Guition ESP32-S3-4848S040 custom firmware

<p align="center">
 <img width="200px" src="https://github.com/alaltitov/display/raw/ff08af58a90efc1293003959ed4ca9c6d12962bf/png/screen3.png">
 <img width="200px" src="https://github.com/alaltitov/display/raw/ff08af58a90efc1293003959ed4ca9c6d12962bf/png/screen2.png">
 <img width="200px" src="https://github.com/alaltitov/display/raw/ff08af58a90efc1293003959ed4ca9c6d12962bf/png/screen1.png">
 <img width="200px" src="https://github.com/alaltitov/display/raw/ff08af58a90efc1293003959ed4ca9c6d12962bf/png/screen0.png">
</p>

<p align="center">
    <img alt="Static Badge" src="https://img.shields.io/badge/made%20by-alaltitov-blue">
    <img alt="Static Badge" src="https://img.shields.io/badge/version-v1.0%20Alpha-green">
    <img alt="Static Badge" src="https://img.shields.io/badge/esphome min version-2024.8.0-red">
    <img alt="Static Badge" src="https://img.shields.io/badge/license-MIT-orange">
</p>

## Features

- Status indicators for Wi-Fi, Home Assistant, thermostat, ventilation, presence sensor, and buzzer
- Animated weather icons with current conditions and temperature
- Date and time
- Screen lock
- Sensor readings from Home Assistant
- Navigation buttons to device control pages (ventilation, vacuum cleaner, and curtains are not implemented yet)
- Thermostat control with built-in display relay
- Control of three light sources:
  * First source from Home Assistant with brightness and color temperature adjustment
  * Second source directly from the display relay
  * Third source from Home Assistant without adjustment
- Settings:
  * Backlight adjustment
  * Screen timeout settings
  * Sound notifications for exceeding sensor thresholds
  * Language selection (English/Russian)

## Instalation

Place all files from src folder into esphome folder of your home assistant. Edit display.yaml file according to your configuration, for example wi-fi and ota fields. Replace entities from home assistant with your own (entity_id).

## Future upcoming updates
- Show/hide sensor on the main screen, configurable from the settings menu

## Future updates
- Flexible configuration of control buttons from the menu
- Selection of the home assistant entity from the settings menu
- Configuration of sensor values ​​for notification
- Additional widgets (ventilation, curtains, vacuum cleaner, smart sockets)

## Documentation

- https://esphome.io/components/lvgl/

### Thanks for your help



Thanks, Clyde and everyone from the ESPHome Discord, for helping me with the project!
