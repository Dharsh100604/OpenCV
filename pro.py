import cv2
import pytesseract

# Load the image using OpenCV
image = cv2.imread('sudoku.png')

# Preprocess the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding
_, threshold = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Perform text extraction
numbers = pytesseract.image_to_string(threshold, config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')

# Print the extracted numbers
print(numbers)
