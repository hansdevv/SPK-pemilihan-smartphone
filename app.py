import streamlit as st
from PIL import Image
from src.models.smartphone import Smartphone

favIcon = Image.open('./src/assets/img/favicon.ico')

st.set_page_config(
	page_title="SPK-Pemilihan-smartphone",
	page_icon=favIcon,
	layout="centered",
	initial_sidebar_state="expanded"
)

hide_menu_style = """
	<style>
	#MainMenu {visibility: hidden;}
	</style>
	"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# untuk menyembunyikan footer
hideFooter = '''
<style>
.css-cio0dv {display: none;}
'''
st.markdown(hideFooter, unsafe_allow_html=True)

def SAW():
	# pass
	uri = st.secrets['MONGO_URI']
	username = st.secrets['mongodb']['username']
	password = st.secrets['mongodb']['password']
	hp = Smartphone(uri,username,password)
	data = hp.show()
	for dt in data:
		st.write(dt)
def WP():
	pass

# Define a function to handle page selection
def main():
	st.sidebar.image(Image.open('./src/assets/img/unjaya.png'),width=300)
	st.sidebar.columns(3)[1].title("UNJAYA")
	selection = st.sidebar.selectbox("Metode",["SAW", "WP"])
	if selection == "SAW":
		SAW()
	elif selection == "WP":
		WP()

if __name__ == '__main__':
	main()