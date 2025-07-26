# Simple OCR Project

This project demonstrates a basic yet effective Optical Character Recognition (OCR) system built using Python. It uses the Tesseract OCR engine, integrated through the `pytesseract` library, along with `OpenCV` for image preprocessing. The core objective of this project is to extract readable printed text from an image using simple image enhancement techniques and then recognize and display the textual content.

The script accepts an input image file containing printed or typed text. It performs several preprocessing steps such as converting the image to grayscale, applying Gaussian blur, adaptive thresholding, and morphological transformations like dilation. These steps help improve the quality of text detection and recognition by enhancing the contrast and structure of the characters in the image.

After preprocessing, the script uses the Tesseract OCR engine to analyze the image and extract the text. The recognized text is then printed to the terminal for the user to read. Additionally, the preprocessed result is saved as a separate image file named `final_output_small.png` for visual verification of the text areas used by the OCR engine.

To run this project, the user needs to have Python installed, along with the required packages: `opencv-python`, `pytesseract`, and `numpy`. It is also essential to have Tesseract installed on the system, and the path to the Tesseract executable must be specified in the script if running on Windows.

This project serves as a beginner-friendly introduction to OCR and image processing. It can be extended further to work with multiple images, scanned PDFs, or even real-time OCR from a webcam. The code is well-commented and modular, making it easy to modify and experiment with different preprocessing techniques or OCR settings.

The project folder includes three files: the input image , the main script (`ocr_script.py`), and this documentation file (`README.md`). It’s a compact and practical tool for students and developers who want to learn the fundamentals of OCR through hands-on coding.

For any questions, contributions, or suggestions, feel free to reach out to the project author:

**Yaqoob Omar**
📧 Email: yaqoobcode@gmail.com  
🌐 GitHub: [YaqoobOmar](https://github.com/YaqoobOmar)  
📍 Based in Hyderabad, Telangana, India
