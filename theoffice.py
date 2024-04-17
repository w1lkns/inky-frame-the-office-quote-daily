import gc
import ujson
from urllib import urequest
from picographics import PicoGraphics, DISPLAY_INKY_FRAME as DISPLAY
import utime
import network
from secrets import WIFI_SSID, WIFI_PASSWORD

graphics = PicoGraphics(DISPLAY)
WIDTH, HEIGHT = graphics.get_bounds()

# Function to connect to the Wi-Fi
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Network config:', sta_if.ifconfig())
    
def disconnect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if sta_if.isconnected():
        print('Disconnecting from network...')
        sta_if.disconnect()
        sta_if.active(False)
        print('Disconnected.')

# Define colors using graphics.create_pen for clarity
BLACK = graphics.create_pen(0, 0, 0)
WHITE = graphics.create_pen(255, 255, 255)
GREY = graphics.create_pen(200, 200, 200)

def sanitize_text(text):
    replacements = {
        "’": "'",  # Replace curly apostrophes with straight ones
        "“": '"',  # Replace left double quotation marks
        "”": '"',  # Replace right double quotation marks
        "…": "...",  # Replace ellipsis with three dots
        "—": "-",  # Replace em-dash with a hyphen
        "–": "-"   # Replace en-dash with a hyphen
    }
    for find, replace in replacements.items():
        text = text.replace(find, replace)
    return text

def get_office_quote():
    gc.collect()
    try:
        response = urequest.urlopen("https://officeapi.akashrajpurohit.com/quote/random")
        raw_data = response.read()
        text = raw_data.decode('utf-8')
        j = ujson.loads(text)
        quote, character = sanitize_text(j['quote']), sanitize_text(j['character'])
        response.close()
        return quote, character
    except Exception as e:
        print("Error fetching quote:", e)
        return None, None

def determine_scale(text, max_width, max_scale=20):
    # Start from the base scale and decrease until the text fits or the minimum scale is reached
    for scale in range(max_scale, 0, -1):
        if graphics.measure_text(text, scale=scale) <= max_width:
            return scale
    return scale  # Use the minimum scale if no suitable scale is found

def display_wrapped_text(text, ox, oy, max_width):
    # Dynamic scale calculation that considers both width and text length
    graphics.set_font("bitmap8")
    scale = 20
    while scale > 1:
        lines = estimate_lines(text, scale, max_width)
        if lines * (15 * scale) <= (HEIGHT - oy - 50):  # Ensuring there's space for character text at the bottom
            break
        scale -= 1

    line_height = 15 * scale
    x, y = ox, oy
    words = text.split()
    space_width = graphics.measure_text(' ', scale=scale)

    for word in words:
        word_width = graphics.measure_text(word, scale=scale)
        if x + word_width + space_width > ox + max_width:
            x = ox  # Start at the beginning of the next line
            y += line_height
        graphics.text(word, x, y, scale=scale)
        x += word_width + space_width

    return y + line_height  # Return the y-coordinate after the last line

def estimate_lines(text, scale, max_width):
    """Estimate how many lines the text will occupy at the given scale."""
    words = text.split()
    x = 0
    lines = 1
    space_width = graphics.measure_text(' ', scale=scale)

    for word in words:
        word_width = graphics.measure_text(word, scale=scale)
        if x + word_width > max_width:
            lines += 1
            x = word_width + space_width
        else:
            x += word_width + space_width

    return lines


def display_quote(quote, character):
    WIDTH, HEIGHT = graphics.get_bounds()
    graphics.set_pen(WHITE)
    graphics.clear()

    # Display the header
    header_text = "The Office - Quote of the Day"
    header_scale = determine_scale(header_text, WIDTH - 20, 5)  # Maintain dynamic scaling for the header
    graphics.set_pen(BLACK)
    graphics.text(header_text, (WIDTH - graphics.measure_text(header_text, scale=header_scale)) // 2, 10, WIDTH, header_scale)

    # Display the quote using the revised wrapped text function
    quote_y_end = display_wrapped_text(quote, 10, 60, WIDTH - 20)

    # Display the character info
    char_scale = determine_scale(character, WIDTH - 20, 4)  # Determine a suitable scale for the character name
    character_y_position = HEIGHT - 50  # Adjust positioning as needed
    graphics.text(character, (WIDTH - graphics.measure_text(character, scale=char_scale)) // 2, character_y_position, WIDTH, char_scale)

    graphics.update()

def main():
    while True:
        quote, character = get_office_quote()
        if quote and character:
            display_quote(quote, character)
            print(quote)            
            
        else:
            print("Failed to fetch a quote, retrying in 10 seconds.")
            utime.sleep(10)
            
        disconnect_wifi()  # Disconnects wifi connection
        utime.sleep(7200)  # Update every 2 hours

if __name__ == "__main__":
    gc.collect()
    connect_wifi()
    main()
