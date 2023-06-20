# ImageConverter

ImageConverter is a Python Packages that provides methods to convert images between different formats, such as bytes and base64 encoding. It uses the OpenCV library for image processing.

## Installation

To use the ImageConverter class, you need to have OpenCV installed. You can install it using pip:

```shell
pip install opencv-python
```

# Usage
First, import the necessary modules:

Then, import and create an instance of the ImageConverter class:


```
converter = ImageConverter()
```

# Loading an Image
To load an image from a file, use the load_image method:

```
converter.load_image('path/to/image.jpg')
```

# Converting Image to Bytes
To convert the loaded image to bytes, use the image_to_bytes method:

```
image_bytes = converter.image_to_bytes()
```

# Converting Bytes to Image
To convert bytes back to an image, use the bytes_to_image method:

```
image = converter.bytes_to_image(image_bytes)
```

# Encoding Image to Base64
To encode the image as a base64 string, use the encode_image_to_base64 method:

```
encoded_image = converter.encode_image_to_base64()
```

# Decoding Base64 to Image
To decode a base64-encoded image back to an image, use the decode_base64_to_image method:

```
decoded_image = converter.decode_base64_to_image(encoded_image)
```

# Saving Decoded Image
To save the decoded image to a file, use the save_decoded_image method:

```
converter.save_decoded_image('path/to/output.jpg')
```

# Examples
Here's an example that demonstrates how to use the ImageConverter class:


```

from image_converter import ImageConverter

# Create an instance of the ImageConverter class
converter = ImageConverter()

# Load an image
converter.load_image('path/to/image.jpg')

# Convert the image to bytes
image_bytes = converter.image_to_bytes()

# Convert bytes back to an image
image = converter.bytes_to_image(image_bytes)

# Encode the image as a base64 string
encoded_image = converter.encode_image_to_base64()

# Decode the base64 image back to an image
decoded_image = converter.decode_base64_to_image(encoded_image)

# Save the decoded image
converter.save_decoded_image('path/to/output.jpg')


```

# Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.


# License
This project is open source and licensed under the MIT License.

# Contact

For any questions or inquiries, please contact:

- Muhammad Tanveer Sultan
- Email: engr.tanveersultan53@gmail.com