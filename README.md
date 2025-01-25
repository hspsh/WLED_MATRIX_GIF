# 🎥 WLED GIF Animator 🎬

This Python script allows you to display GIF animations on WLED-managed LEDs. The script processes each frame of the GIF, increases the contrast and sends the data to the WLED controller.

## 🛠 Requirements

- Python 3.x
- Library `Pillow` for the handling of images
- Library `socket` for network communication

## 📦 Installation

1. **Install the required libraries:**

   ```bash
   pip install Pillow
   ```

2. **Clone repository:**

## ⚙ Configuration

1. **Set the IP address of your WLED controller:**


   ```python
   WLED_IP = "192.168.88.55"  # 👈 
   ```

2. **Path to GIF file.:**

   ```python
   GIF_FILE_PATH = r"file.gif"  # 👈 
   ```

3. **Adjust contrast gain level:**

  You can adjust the level of contrast enhancement by changing the value of the variable`IMG_ENHANCE_LV`.

   ```python
   IMG_ENHANCE_LV = 2  # 👈 Dostosuj poziom kontrastu
   ```

## 🚀 Run

To run the script, execute the following command:

```bash
python skrypt.py
```
