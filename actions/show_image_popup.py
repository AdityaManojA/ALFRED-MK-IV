# actions/show_image_popup.py
"""
Action to show an image popup overlay.
"""

from __future__ import annotations

import os
from pathlib import Path

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal

from ui import tech_font, mono_font, C


class ImagePopupOverlay(QWidget):
    """Popup overlay to display an image with a dismiss button."""

    dismissed = pyqtSignal()

    def __init__(self, image_path: str, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setStyleSheet(f"""
            ImagePopupOverlay {{
                background: {C.PANEL_BG};
                border: 1px solid {C.BORDER_B};
                border-radius: 4px;
            }}
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        # Image label
        self._image_label = QLabel()
        self._image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            # Scale image to fit reasonably, max width/height 400px while keeping aspect ratio
            scaled = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self._image_label.setPixmap(scaled)
        else:
            self._image_label.setText(f"[Image not found: {image_path}]")
            self._image_label.setStyleSheet(f"color: {C.TEXT_MED};")
        layout.addWidget(self._image_label)

        # Dismiss button
        dismiss_btn = QPushButton("Dismiss")
        dismiss_btn.setFont(tech_font(9, QFont.Weight.Bold))
        dismiss_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        dismiss_btn.setFixedHeight(28)
        dismiss_btn.setStyleSheet(f"""
            QPushButton {{
                background: {C.PRI};
                color: {C.DARK};
                border: 1px solid {C.PRI};
                border-radius: 2px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background: {C.TEXT_BRIGHT};
                color: #000000;
                border-color: #ffffff;
            }}
            QPushButton:pressed {{
                background: {C.PRI_DIM};
                color: {C.DARK};
            }}
        """)
        dismiss_btn.clicked.connect(self.hide)
        dismiss_btn.clicked.connect(self.dismissed.emit)
        layout.addWidget(dismiss_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    def show_centered(self, parent: QWidget):
        """Show the popup centered over the parent widget."""
        if parent:
            self.move(
                parent.x() + (parent.width() - self.width()) // 2,
                parent.y() + (parent.height() - self.height()) // 2,
            )
        self.show()
        self.raise_()
        self.activateWindow()


def action(parameters: dict, player=None, speak=None, response=None, session_memory=None) -> str:
    """Show an image popup overlay."""
    image_path = parameters.get("image_path")
    if not image_path:
        return "Error: image_path parameter is required for show_image_popup action."

    # Resolve relative paths relative to the project root
    if not os.path.isabs(image_path):
        # Assume relative to the project root (two levels up from this file)
        project_root = Path(__file__).resolve().parent.parent
        image_path = str((project_root / image_path).resolve())

    if not os.path.exists(image_path):
        return f"Error: Image file not found: {image_path}"

    if player is None:
        return "Error: Player context not available to show overlay."

    # Get the central widget to parent the overlay
    central_widget = player.centralWidget()
    if central_widget is None:
        return "Error: Could not get central widget."

    # Create and show the overlay
    overlay = ImagePopupOverlay(image_path, parent=central_widget)
    # Keep a reference to prevent garbage collection
    player._image_popup_overlay = overlay
    overlay.show_centered(central_widget)

    return f"Showing image popup: {image_path}"


TOOL = {
    "name": "show_image_popup",
    "description": "Show an image popup overlay with a dismiss button. Parameters: image_path (string, path to image file).",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "image_path": {
                "type": "STRING",
                "description": "Path to the image file to display (can be relative to project root)."
            }
        },
        "required": ["image_path"]
    },
    "scheduling": "WHEN_IDLE",  # Does not block speech
    "handler": action
}