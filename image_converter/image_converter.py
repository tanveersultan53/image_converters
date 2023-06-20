import cv2
import base64
import numpy as np


class ImageConverter:
    def __init__(self) -> None:
        """
        Initializes the ImageConverter class.
        """
        self.image_path = None
        self.image = None

    def load_image(self, image_path: str) -> None:
        """
        Loads an image from the specified path.

        Args:
            image_path (str): The path to the image file.
        """
        self.image_path = image_path
        self.image = cv2.imread(image_path)

    def image_to_bytes(self) -> bytes:
        """
        Converts the image to bytes.

        Returns:
            bytes: The image data represented as bytes.
        """
        _, img_bytes = cv2.imencode('.jpg', self.image)
        img_bytes = img_bytes.tobytes()
        return img_bytes

    def bytes_to_image(self, img_bytes: bytes) -> np.ndarray:
        """
        Converts bytes back to an image.

        Args:
            img_bytes (bytes): The image data represented as bytes.

        Returns:
            numpy.ndarray: The decoded image.
        """
        decoded_image = base64.b64decode(img_bytes)
        nparr = np.frombuffer(decoded_image, np.uint8)
        decoded_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return decoded_image

    def encode_image_to_base64(self) -> str:
        """
        Encodes the image to base64.

        Returns:
            str: The encoded image as a base64 string.
        """
        img_bytes = self.image_to_bytes()
        encoded_image = base64.b64encode(img_bytes)
        return encoded_image

    def decode_base64_to_image(self, encoded_image: str) -> np.ndarray:
        """
        Decodes the base64 image back to an image.

        Args:
            encoded_image (str): The base64-encoded image.

        Returns:
            numpy.ndarray: The decoded image.
        """
        decoded_image = base64.b64decode(encoded_image)
        nparr = np.frombuffer(decoded_image, np.uint8)
        decoded_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return decoded_image

    def save_decoded_image(self, output_path: str) -> None:
        """
        Decodes the base64 image and saves it to the specified output path.

        Args:
            output_path (str): The path to save the decoded image.
        """
        if self.image is None:
            raise ValueError("No image loaded. Use 'load_image' method to load an image.")

        decoded_image = self.decode_base64_to_image(self.encode_image_to_base64())
        cv2.imwrite(output_path, decoded_image)