import streamlit as st
from PIL import Image
from agent import CropDiseaseAgent

# Create the AI agent
agent = CropDiseaseAgent()

st.set_page_config(
    page_title="AI-Based Crop Disease Detection",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 AI-Based Crop Disease Detection")
st.write("Upload a crop leaf image to detect possible diseases.")

# Image upload
uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Leaf",
        use_container_width=True
    )

    # Demo prediction
    # Replace this part later with your trained AI model
    disease = "Bacterial Spot"
    confidence = 86

    # Send prediction to agent
    result = agent.analyze_disease(
        disease,
        confidence
    )

    # -----------------------------
    # Display Results
    # -----------------------------

    st.success(
        f"🦠 Disease: {result['Disease']}"
    )

    st.info(
        f"📊 Confidence: {result['Confidence']}"
    )

    st.subheader("🔍 Symptoms")
    st.write(result["Symptoms"])

    st.subheader("🦠 Disease Cause / Bacteria Name")
    st.write(result["Cause"])

    st.subheader("💊 Treatment")
    st.write(result["Treatment"])

    st.subheader("🛡️ Prevention")
    st.write(result["Prevention"])

    st.subheader("🧪 Recommended Pesticides")
    st.write(result["Pesticides"])

    st.subheader("📋 Pesticide Usage")
    st.write(result["Usage"])

    st.subheader("🔧 How to Solve the Problem")
    st.write(result["Solution"])

    st.subheader("🌾 Recommendations")

    for recommendation in result["Recommendations"]:
        st.write("✅", recommendation)

else:
    st.warning("Please upload a crop leaf image.")