# pylint: disable=C0114,E1101 # hardware specific modules cannot be imported
"""Badge generator for Badger2040W e-ink display.

This module provides functionalities to create and display customized badges on the 
Badger2040W e-ink screen. It allows users to configure various elements such as company names,
personal names, detailed information, and QR codes to produce comprehensive and visually
appealing badges.

Features:
- **Customizable Layout**: Define the placement and size of company logos, personal names,
 and details.
- **QR Code Integration**: Generate and embed QR codes for easy access to digital information.
- **Adjustable Text Sizes**: Configure text sizes to fit different sections of the badge.
- **Optimized Display Updates**: Utilize Badger2040's update speeds to balance clarity
 and performance.
- **Image Handling**: Placeholder for images allowing the inclusion of graphical elements.

Usage:
1. **Configuration**: Modify the global constants to set dimensions, text sizes, and other
display parameters.
2. **Generation**: Run the main script to generate the badge layout based on the
configured settings.
3. **Display**: The badge is rendered on the Badger2040W e-ink display, ready for use.

Dependencies:
- `badger2040`: Library for interfacing with the Badger2040W hardware.
- `math`: For mathematical operations related to layout calculations.
- `src.assets.qr.bit_matrix`: Module for generating QR codes.

Example:
```python
import badger2040
from src.assets.qr.bit_matrix import BIT_MATRIX

def draw_badge():
    badge = badger2040.Badger2040()
    badge.set_update_speed(badger2040.UPDATE_FAST)
    badge.update()
    # Add additional drawing logic here
```

This module serves as the backbone for generating customizable badges, making it easy
to produce professional and functional e-ink displays for various applications.
"""

import math
import badger2040  # type: ignore # noqa: F401

from src.assets.qr.bit_matrix import BIT_MATRIX

""""""
# BADGE DISPLAY DIMENSIONS DIAGRAM ######################
#
#                       296px width
# ┌───────────────────────────────┬─────────────────────┐
# │            company            │█████████████████████│
# │           167 x 30            │█████████████████████│
# ├───────────────────────────────┤█████████████████████│
# │                               │█████████████████████│
# │             name              │█████████████████████│   128px
# │           167 x 58            │██IMAGE_PLACEHOLDER██│  height
# │                               │██████128 x 128██████│
# │                               │█████████████████████│
# ├───────────────────────────────┤█████████████████████│
# │       DETAILS1 167 x 20       │█████████████████████│
# ├───────────────────────────────┤█████████████████████│
# │       DETAILS2 167 x 20       │█████████████████████│
# └───────────────────────────────┴─────────────────────┘
""""""


# ------------------------------
#       Constants Definitions
# ------------------------------


# Global Constants
WIDTH = badger2040.WIDTH  # 296
HEIGHT = badger2040.HEIGHT  # 128

# Image/QR constants
IMAGE_QR_WIDTH = 128
IMAGE_QR_HEIGHT = HEIGHT

# Company constants
COMPANY_HEIGHT = 30

# Details constants
DETAILS_HEIGHT = 20

# Name constants
NAME_HEIGHT = HEIGHT - COMPANY_HEIGHT - (DETAILS_HEIGHT * 2) - 2

# Text constants
TEXT_WIDTH = WIDTH - IMAGE_QR_WIDTH - 1

COMPANY_TEXT_SIZE = 0.6
DETAILS_TEXT_SIZE = 0.5

LEFT_PADDING = 5
NAME_PADDING = 20
DETAIL_SPACING = 10

CONTENT_PATH = "//src/content.txt"

DEFAULT_TEXT = """COMPANY_NAME
ATTENDEE_NAME
DETAILS1_TITLE
DETAILS1_VALUE
DETAILS2_TITLE
DETAILS2_VALUE
"""

# ------------------------------
#        Program setup
# ------------------------------

# Create a new Badger and set it to update NORMAL
display = badger2040.Badger2040()
display.led(5)  # int: 0 (off) to 255 (full)
display.set_update_speed(0)  # int: 0 = normal, 1 + medium, 2 = fast, 3 = turbo

# Thickness affects Hershey text and governs how thick the component lines should be
display.set_thickness(2)


# ------------------------------
#        Read content.txt
# ------------------------------

try:
    badge_contents = open(CONTENT_PATH, "r", encoding="utf-8")
except OSError:
    with open(CONTENT_PATH, "w", encoding="utf-8") as f:
        f.write(DEFAULT_TEXT)
        f.flush()
badge_contents = open(CONTENT_PATH, "r", encoding="utf-8")

# Read in the next 6 lines
company_name = badge_contents.readline().strip()  # txt_COMPANY_NAME
attendee_name = badge_contents.readline().strip()  # txt_ATTENDEE_NAME
detail1_title = badge_contents.readline().strip()  # txt_DETAILS1_TITLE
detail1_text = badge_contents.readline().strip()  # txt_DETAILS1_TEXT
detail2_title = badge_contents.readline().strip()  # DETAILS2_TITLE
detail2_text = badge_contents.readline().strip()  # txt_DETAILS2_TEXT

# ------------------------------
#        Helper functions
# ------------------------------


def truncatestring(text, text_size, width):
    """
    Truncates a given text to fit within a specified width.

    Parameters:
    - text (str): The text to be truncated.
    - text_size (int): The size of the text.
    - width (int): The maximum width allowed for the text.

    Returns:
    - str: The truncated text.

    Explanation:
    This function takes a text, its size, and a width as input parameters.
    It repeatedly removes the last character from the text until the length
    of the text exceeds the specified width. Once the length is within the
    limit, the function returns the truncated text.
    """
    while True:
        length = display.measure_text(text, text_size)
        if length > 0 and length > width:
            text = text[:-1]
        else:
            text += ""
            return text


# ------------------------------
#        Section functions
# ------------------------------


def draw_company(company_text: str) -> None:
    """Draw the company name on the badge."""


def draw_name(attendee_name: str) -> None:
    """Draw the attendee name on the badge."""


def draw_detail1(detail1_title: str, detail1_text: str) -> None:
    """Draw the first detail section on the badge."""


def draw_detail2(detail2_title: str, detail2_text: str) -> None:
    """Draw the second detail section on the badge."""


def draw_qr_code():
    """Draw the QR code on the badge."""

    # TODO: Check if it's better to load an image or to draw the QR code

    # Get the dimensions of the bit matrix
    y_length = len(BIT_MATRIX)
    x_length = len(BIT_MATRIX[0]) if y_length > 0 else 0

    # Calculate the size of each bit in the QR code
    qr_bit_x_width = IMAGE_QR_WIDTH // x_length
    qr_bit_y_width = IMAGE_QR_HEIGHT // y_length

    # Calculate the padding for the QR code
    x_padding = math.ceil((IMAGE_QR_WIDTH % (IMAGE_QR_WIDTH // x_length) / 2))
    y_padding = math.ceil((IMAGE_QR_HEIGHT % (IMAGE_QR_HEIGHT // y_length) / 2))

    for row, bit_row in enumerate(BIT_MATRIX):
        for col, bit in enumerate(bit_row):
            x = WIDTH - IMAGE_QR_WIDTH + x_padding + col * 5
            y = 0 + y_padding + row * 5
            display.set_pen(bit)
            display.rectangle(x, y, qr_bit_x_width, qr_bit_y_width)

    display.partial_update(
        WIDTH - IMAGE_QR_WIDTH,  # int: x coordinate of the update region
        0,  # int: y coordinate of the update region (must be a multiple of 8)
        IMAGE_QR_WIDTH,  # int: width of the update region
        IMAGE_QR_HEIGHT,  # int: height of the update region (multiple of 8)
    )


# ------------------------------
#        Draw the badge
# ------------------------------


def draw_badge():
    """Draw the complete badge layout.

    This function handles drawing all elements of the badge in the correct order:
    1. Clears the display to white
    2. Draws the company name section
    3. Draws the attendee name
    4. Draws the first detail section
    5. Draws the second detail section
    6. Draws the QR code

    The function uses the global display object to render all elements and handles
    both full and partial screen updates as needed.
    """
    display.set_pen(15)
    display.clear()  # Fills the drawing buffer with the pen colour, giving you a clean slate
    display.update()  # Let's paint the screen white

    # draw_company(company_name)
    # draw_name(attendee_name)
    # draw_detail1(detail1_title, detail1_text)
    # draw_detail2(detail2_title, detail2_text)
    draw_qr_code()
    # display.update()

    # TODO Check if the load order is efficient
