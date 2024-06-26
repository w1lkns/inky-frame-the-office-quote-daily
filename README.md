# The Office Quote Display

This project is designed to fetch and display quotes from "The Office" on an Inky Frame display, utilizing a PicoGraphics library. It connects to a public API to retrieve quotes and attributes them to their respective characters from the show.

## Features

- **Automatic Quote Fetching**: Connects to "The Office" API and fetches a new quote every 6 hours.
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
``` git clone https://github.com/w1lkns/office-quote-display.git ```
3. Ensure all dependencies are installed and compatible with your microcontroller.
4. Connect your microcontroller to your MicroPython editor - i.e -> Thonny
5. Update the `secrets.py` with your Wi-Fi credentials:

```
WIFI_SSID = "yourSSID"
WIFI_PASSWORD = "yourPassword"
```

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

## Acknowledgments

This project utilizes the "The Office" Quote API created by Akash Rajpurohit. The API is freely available and offers a wide range of quotes from "The Office" (US version). For more information about the API and to explore other projects, visit the [official API documentation](https://officeapi.akashrajpurohit.com/).

### API Details

- **API Home**: [The Office API](https://officeapi.akashrajpurohit.com/)
- **API Endpoint Used**: `https://officeapi.akashrajpurohit.com/quote/random`
- **API Description**: This API endpoint provides random quotes from the TV show "The Office", which are used in this project to display on an Inky Frame via a Raspberry Pi Pico.

## Using the API

To use this API in your projects, you can make HTTP GET requests to the endpoint mentioned above. Here is an example of how to fetch data from the API:

```python
import urequest

def fetch_office_quote():
    url = "https://officeapi.akashrajpurohit.com/quote/random"
    response = urequest.urlopen(url)
    data = response.read()
    return data

quote_data = fetch_office_quote()
print(quote_data)
```

