from setuptools import setup

setup(
    name='image_converters',
    version='0.1.0',
    description='ImageConverter is a Python Package that provides methods to convert images between different formats, '
                'such as bytes and base64 encoding. It uses the OpenCV library for image processing.',
    author='Tanveer Sultan',
    author_email='engr.tanveersultan53@gmail.com',
    url='https://github.com/tanveersultan53/image_converters',
    packages=['image_converter'],
    install_requires=['opencv-python', 'numpy'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
