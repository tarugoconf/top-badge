"""
QR code generator.

This module generates a 25x25 QR code matrix to use in eink badge and saves it to a Python file.
The output matrix uses 0 for black pixels and 15 for white pixels.

Dependencies:
    - qrcode
    - numpy
"""

import os

import qrcode  # https://pypi.org/project/qrcode/
import qrcode.constants
import numpy as np  # https://pypi.org/project/numpy/

# QR Code configuration
QR_VERSION = 2  # 25x25 matrix
QR_ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_L
QR_BORDER = 0
QR_BLACK_VAL = 0
QR_WHITE_VAL = 15
QR_EXPECTED_DIMENSIONS = (25, 25)


# Define the data to encode in the QR code.
# You can encode various types of data in a QR code. Here are some examples:
# 1. URL:
DATA = "https://example.com"

# 2. Contact Information (vCard):
# DATA = """
# BEGIN:VCARD
# VERSION:3.0
# N:Doe;John;;;
# FN:John Doe
# ORG:Example Company
# TEL;TYPE=WORK,VOICE:(111) 555-1212
# EMAIL:johndoe@example.com
# END:VCARD
# """

# 3. Wi-Fi Configuration:
# DATA = "WIFI:T:WPA;S:ExampleSSID;P:password123;;"

# 4. Geolocation:
# DATA = "geo:37.7749,-122.4194"


def create_qr_matrix(data):
    """Generates a 25x25 QR code matrix
    Args:
        data: Text string to encode in the QR code.

    Returns:
        List of lists containing the QR code matrix values (0 or 15).

    Raises:
        ValueError: If data is empty or too long for QR version 2
    """
    if not data:
        raise ValueError("Data cannot be empty")

    # Create QR code instance with version 2 for a 25x25 matrix
    qr = qrcode.QRCode(
        version=QR_VERSION,
        error_correction=QR_ERROR_CORRECTION,
        border=QR_BORDER,
    )

    # Add data to QR
    qr.add_data(data)
    qr.make(fit=True)

    # Get the QR matrix
    matrix = np.array(qr.get_matrix(), dtype=np.uint8)

    # Convert boolean matrix to 0s and 15s
    matrix = matrix * QR_WHITE_VAL

    # Convert the matrix to a list of lists
    matrix = matrix.tolist()

    # Verify matrix dimensions
    if len(matrix) != QR_EXPECTED_DIMENSIONS[0] or any(
        len(row) != QR_EXPECTED_DIMENSIONS[1] for row in matrix
    ):
        msg = (
            f"Expected {QR_EXPECTED_DIMENSIONS[0]}x{QR_EXPECTED_DIMENSIONS[1]} "
            f"matrix, got {len(matrix)}x{len(matrix[0])}"
        )
        raise ValueError(msg)

    return matrix


def write_bit_matrix(
    matrix, output_file=os.path.join(os.path.dirname(__file__), "bit_matrix.py")
):
    """Writes the QR code matrix to a Python file.

    Args:
        matrix: List of lists containing the QR code matrix values
        output_file: Path to output file (default: src/assets/qr/bit_matrix.py)
    """
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(
                '"""\nQRCode bit matrix module containing the matrix representation of a QR code.\n'
            )
            f.write("Each cell is represented by either 0 (black) or 15 (white).\n")
            f.write(
                f'This matrix has been generated by "{os.path.basename(__file__)}"\n"""\n\n'
            )
            f.write("BIT_MATRIX = [\n")
            for matrix_row in matrix:
                f.write(f"    {matrix_row},\n")
            f.write("]\n")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")
        raise


def main(data=DATA, output_file=None):
    """Main function to generate QR code matrix

    Args:
        data: URL or text to encode (default: DEFAULT_URL)
        output_file: Optional custom output file path
    """
    matrix = create_qr_matrix(data)
    if output_file:
        write_bit_matrix(matrix, output_file)
    else:
        write_bit_matrix(matrix)


if __name__ == "__main__":
    main()