import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFileDialog, QLabel


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_path = None  # Stores the path to the selected image
        self.image_label = QLabel()  # Label to display the image

        # Button to select image
        self.select_button = QPushButton("Select Image")
        self.select_button.clicked.connect(self.open_file_dialog)

        # Layout
        layout = QMainWindow.layout(self)
        layout.addWidget(self.select_button)
        layout.addWidget(self.image_label)

    def open_file_dialog(self):
        # Open file dialog with image filters
        filters = "Images (*.png *.jpg *.jpeg)"
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", filters)

        # Check if an image is selected
        if self.image_path:
            # Load the image and set it to the label
            self.image_label.setPixmap(QPixmap(self.image_path))
            self.show()  # Update the window content

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
