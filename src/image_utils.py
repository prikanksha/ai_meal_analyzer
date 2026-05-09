import base64
import io

from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def image_to_base64(uploaded_file):
  image = Image.open(uploaded_file)
  buffer = io.BytesIO()
  image.convert("RGB").save(buffer, format="JPEG")
  return base64.b64encode(buffer.getvalue()).decode('utf-8')