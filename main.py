
import qrcode
import os

url = input("Enter the URL: ").strip()

# Save directly inside your qrcode folder
folder_path = r"C:\Users\haris\OneDrive\Desktop\day 2"
os.makedirs(folder_path, exist_ok=True)

file_path = os.path.join(folder_path, "qrcode.png")

img = qrcode.make(url)
img.save(file_path)

print("QR Code generated successfully!")
print("Saved location:", file_path)
print("File exists:", os.path.exists(file_path))