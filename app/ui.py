# import streamlit as st
# from summarizer import summarize_text

# st.set_page_config(page_title="QuickSummarize", layout="centered")

# st.title("🧠 QuickSummarize - Text Summarizer")
# st.write("Paste your text or upload a `.txt` file to summarize.")

# text_input = st.text_area("Paste your text here", height=250)

# uploaded_file = st.file_uploader("...or upload a .txt file", type=["txt"])
# if uploaded_file is not None:
#     text_input = uploaded_file.read().decode("utf-8")

# if text_input:
#     if st.button("Generate Summary"):
#         summary = summarize_text(text_input)
#         edited_summary = st.text_area("✍️ Editable Summary", value=summary, height=200)
#         st.success("Summary generated! You can now edit it above.")

#         if st.button("Download Summary"):
#             st.download_button("Download as .txt", edited_summary, file_name="summary.txt", mime="text/plain")
import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="QuickSummarize", layout="centered")

st.title("🧠 QuickSummarize - Text Summarizer")
st.write("Paste your text or upload a `.txt` file to summarize.")

# Text input section
text_input = st.text_area("Paste your text here", height=250)

# File upload section
uploaded_file = st.file_uploader("...or upload a .txt file", type=["txt"])
if uploaded_file is not None:
    text_input = uploaded_file.read().decode("utf-8")

# Always visible Generate Summary button
if st.button("Generate Summary"):
    if text_input.strip():  # Ensure text is not empty
        summary = summarize_text(text_input)
        st.session_state["generated_summary"] = summary
        st.session_state["edit_mode"] = False
    else:
        st.warning("Please provide some text before generating the summary.")

# Show summary if generated
if "generated_summary" in st.session_state:
    st.subheader("📝 Summary")

    if st.session_state.get("edit_mode", False):
        # Editable mode
        edited_summary = st.text_area("✍️ Editable Summary", value=st.session_state["generated_summary"], height=200)
        st.session_state["generated_summary"] = edited_summary

        if st.button("Save Changes"):
            st.session_state["edit_mode"] = False
            st.success("Summary saved.")
    else:
        # Read-only mode
        st.text_area("Summary (Read-only)", value=st.session_state["generated_summary"], height=200, disabled=True)
        if st.button("Edit Summary"):
            st.session_state["edit_mode"] = True

    # Download button (always shown after summary)
    st.download_button("Download as .txt", st.session_state["generated_summary"], file_name="summary.txt", mime="text/plain")
