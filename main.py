import streamlit as st

st.set_page_config(page_title="Popup Example", layout="centered")

# Popup HTML with CSS
popup_html = """
<style>
.popup {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}
.popup-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  max-width: 300px;
}
.popup img {
  max-width: 100%;
}
.button {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  display: inline-block;
  border-radius: 5px;
}
.button:hover {
  background-color: #0056b3;
}
</style>

<div class="popup" id="popup">
  <div class="popup-content">
    <img src="https://i.ibb.co/jyL6vYZ/manga.png" alt="Manga Ad">
    <p>جميع الفصول حصريا على hmanga reader APP</p>
    <a class="button" href="https://your-ad-link.com" target="_blank">Download</a>
    <br><br>
    <a href="#" onclick="document.getElementById('popup').style.display='none'; return false;">Hide</a>
  </div>
</div>
"""

# Inject popup
st.markdown(popup_html, unsafe_allow_html=True)

st.write("Welcome to my Streamlit site!")
