import cv2
import pytesseract

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
image_path = r"C:\Users\yaqoo\Desktop\simple_ocr_project\kargil_image.png"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("Image not loaded.")

# Resize for better OCR (internal use)
image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Preprocess
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    cv2.THRESH_BINARY, 31, 2
)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# OCR
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(processed, config=custom_config)
print("Extracted Text:\n", text)

# Resize the processed image for display (e.g., width=600)
display_width = 600
aspect_ratio = processed.shape[0] / processed.shape[1]
display_height = int(display_width * aspect_ratio)
resized_output = cv2.resize(processed, (display_width, display_height))

# Show the resized processed image
cv2.imshow("Processed (Resized)", resized_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
