# boot.py -- run this to start the badge
"""
boot.py

This script serves as the entry point for the badge application.
When executed, it imports the main module and invokes the `draw_badge` function
to render the badge's display on the Badger2040W e-ink screen.

Usage:
    Run this script to initialize and display the badge based on the
    configured settings in `src.main`.
"""

import src.badge

src.badge.draw_badge()
