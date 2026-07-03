# QRCodePOC
Generates QR Codes for Feedback

# Bill QR Code Generator for Feedback

A lightweight, interactive Streamlit web application that generates QR codes for feedback forms based on validated bill numbers. This tool ensures data integrity by enforcing a strict alphanumeric format for bill numbers before generating the QR code.

## 🚀 Live Demo
👉 [View Live App](https://qrcode-feedback-poc.streamlit.app/)

---

## ✨ Features
* **Format Validation:** Automatically ensures the entered bill number consists of exactly 4 alphabetic characters followed by numeric digits (e.g., `ABCD12345`).
* **Dynamic QR Generation:** Instantly creates high-quality QR codes mapping to your target feedback URL.
* **Streamlined UI:** Built with Streamlit for a fast, responsive, and intuitive user experience.
* **In-Memory Rendering:** Optimized image processing using `io.BytesIO` to prevent server-side rendering errors.

---

## 🛠️ Tech Stack
* **Frontend/Framework:** [Streamlit](https://streamlit.io/)
* **QR Code Generation:** [qrcode](https://pypi.org/project/qrcode/)
* **Image Processing:** [Pillow (PIL)](https://pillow.readthedocs.io/)

---

## 💻 Local Installation & Setup

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
