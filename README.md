# The Office Quote Display

This project is designed to fetch and display quotes from "The Office" on an Inky Frame display, utilizing a PicoGraphics library. It connects to a public API to retrieve quotes and attributes them to their respective characters from the show.

## Features

- **Automatic Quote Fetching**: Connects to "The Office" API and fetches a new quote every 2 hours.
- **Wi-Fi Connectivity**: Manages Wi-Fi connections to fetch quotes and disconnects afterwards to conserve power.
- **Text Sanitization**: Processes and sanitizes text to ensure compatibility with the Inky Frame display limitations.
- **Error Handling**: Robust error handling to manage potential network issues or data errors.
- **Power Efficiency**: Optimizes power usage by managing display and network connectivity.

## Hardware Requirements

- Raspberry Pi Pico or similar MicroPython-capable microcontroller
- Inky Frame display module
- Wi-Fi module compatible with MicroPython

## Software Dependencies

- `ujson`
- `picographics`
- `urllib`
- `network` module for Wi-Fi management

## Installation

1. Clone this repository to your local machine or directly to your microcontroller:
git clone https://github.com/yourusername/office-quote-display.git
2. Ensure all dependencies are installed and compatible with your microcontroller.
3. Update the `secrets.py` with your Wi-Fi credentials:

WIFI_SSID = "yourSSID"
WIFI_PASSWORD = "yourPassword"

## Usage
Once deployed and running, the device will:

1. Connect to the Wi-Fi.
2. Fetch a quote from "The Office" API.
3. Display the quote on the Inky Frame.
4. Disconnect from Wi-Fi to save power.
5. Repeat the process every 2 hours.

## Contributing
Contributions to this project are welcome! Please consider the following steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit them (git commit -am 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a new Pull Request.

## License
This project is licensed under the MIT License
