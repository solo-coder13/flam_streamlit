
import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="AI Person Compositor", layout="centered")
st.title("📸 Seamless Person Compositor")

st.write("Upload a person image and a background scene. The app will automatically composite the person into the scene.")

person_file = st.file_uploader("Upload Person Image", type=["jpg", "jpeg", "png"])
bg_file = st.file_uploader("Upload Background Image", type=["jpg", "jpeg", "png"])

if person_file and bg_file:
    person_img = Image.open(person_file).convert("RGBA")
    bg_img = Image.open(bg_file).convert("RGBA")

    st.image(person_img, caption="Person Image", width=300)
    st.image(bg_img, caption="Background Image", width=400)

    # Remove background from person
    person_no_bg = remove(person_img)

    # Resize and position
    person_resized = person_no_bg.resize((150, 300))
    position = (500, 300)

    # Composite
    result = bg_img.copy()
    result.paste(person_resized, position, person_resized)

    st.markdown("### 🖼 Final Composite Image")
    st.image(result, use_column_width=True)

    # Download button
    img_bytes = io.BytesIO()
    result.save(img_bytes, format="PNG")
    st.download_button("📥 Download Composite", data=img_bytes.getvalue(), file_name="final_composite.png", mime="image/png")
