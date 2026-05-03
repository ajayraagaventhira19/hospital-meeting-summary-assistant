import streamlit as st
import requests

st.set_page_config(
    page_title="Hospital Meeting Assistant",
    layout="centered"
)

st.title("🏥 Hospital Meeting Summary Assistant")
st.write("Upload hospital meeting audio and generate summary")

uploaded_file = st.file_uploader(
    "Upload Meeting Audio",
    type=["mp3", "wav"]
)

if uploaded_file:
    st.success("File uploaded successfully")

    if st.button("Generate Summary"):

        with st.spinner("Processing audio..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    uploaded_file.type
                )
            }

            response = requests.post(
                "http://127.0.0.1:8000/upload-audio/",
                files=files
            )

            result = response.json()

            st.subheader("Transcript")
            st.write(result["transcript"])

            st.subheader("Summary")
            st.write(result["summary"])
