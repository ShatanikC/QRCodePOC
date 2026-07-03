import streamlit as st,qrcode,io
st.set_page_config(layout='centered', page_title="Feedback Form QR Code Generator", page_icon=":memo:")
st.header("Feedback Form QR Code Generator")
bill_number = st.text_input("Enter your Bill Number:", key="feedback_input")
base_url=f'https://docs.google.com/forms/d/e/1FAIpQLSennga8WJziQroP5OBpNQNXicZ1qkJIBn4UM2dmr49otQZlrA/viewform?usp=pp_url&entry.2089953657={bill_number}'
if st.button("Generate QR Code"):
    if bill_number:
        alpha=bill_number[:4]
        if alpha.isalpha():
            digits=bill_number[4:]
            if digits.isdigit():
                qr = qrcode.make(base_url)
                buf = io.BytesIO()
                qr.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.image(byte_im, caption='QR Code for Feedback Form',use_container_width=True)
            else:
                st.error("The last part of the bill number should be digits.")
        else:
            st.error("The first four characters of the bill number should be letters.")
    else:
        st.warning("Please enter a valid Bill Number.")