import cv2
import numpy as np
import argparse
import logging
import os

# Setup professional logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class AdvancedCartoonifier:
    """A professional class to convert images into high-quality cartoon styles."""

    def __init__(self, blur_value=7, line_size=7, color_reduction=9):
        self.blur_value = blur_value
        self.line_size = line_size
        self.color_reduction = color_reduction

    def _get_edges(self, img: np.ndarray) -> np.ndarray:
        """Applies advanced edge detection techniques."""
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.medianBlur(gray, self.blur_value)

        # Detect and enhance edges
        edges = cv2.adaptiveThreshold(
            gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY, self.line_size, self.blur_value
        )
        return edges

    def _color_quantization(self, img: np.ndarray) -> np.ndarray:
        """Reduces the color palette to give a flat, posterized cartoon look."""
        data = np.float32(img).reshape((-1, 3))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
        _, label, center = cv2.kmeans(data, self.color_reduction, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        center = np.uint8(center)
        result = center[label.flatten()]
        result = result.reshape(img.shape)
        return result

    def process_image(self, input_path: str, output_path: str, style: str = "classic"):
        """Loads the image, applies the selected style, and saves the output."""
        if not os.path.exists(input_path):
            logging.error(f"Image not found at {input_path}. Please check the path.")
            return

        # 1. Load input images using OpenCV
        logging.info(f"Loading image from {input_path}...")
        img = cv2.imread(input_path)

        if style == "classic":
            # 2. Apply edge detection techniques
            logging.info("Applying edge detection...")
            edges = self._get_edges(img)

            # 3. Smooth color regions for cartoon effect
            logging.info("Smoothing color regions...")
            quantized = self._color_quantization(img)
            smoothed = cv2.bilateralFilter(quantized, d=9, sigmaColor=200, sigmaSpace=200)

            # 4. Combine edges with smoothed image
            logging.info("Combining edges with smoothed colors...")
            cartoon = cv2.bitwise_and(smoothed, smoothed, mask=edges)

        elif style == "watercolor":
            # Bonus Out-of-the-box feature!
            logging.info("Applying watercolor stylization...")
            cartoon = cv2.stylization(img, sigma_s=60, sigma_r=0.6)

        else:
            logging.error("Invalid style selected.")
            return

        # 5. Save final cartoonified images
        cv2.imwrite(output_path, cartoon)
        logging.info(f"Success! Cartoonified image saved to: {output_path}")

if __name__ == "__main__":
    # Setup Command Line Interface (CLI)
    parser = argparse.ArgumentParser(description="High-Tech Image Cartoonifier")
    parser.add_argument("-i", "--input", required=True, help="Path to the original input image")
    parser.add_argument("-o", "--output", default="output_cartoon.jpg", help="Path to save the generated image")
    parser.add_argument("-s", "--style", choices=["classic", "watercolor"], default="classic", help="Choose the cartoon style (classic or watercolor)")

    args = parser.parse_args()

    # Execute the application
    app = AdvancedCartoonifier()
    app.process_image(args.input, args.output, args.style)