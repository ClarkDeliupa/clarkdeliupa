import streamlit as st
from PIL import Image

st.set_page_config(page_title="Clark Justin's Website", page_icon=":tada:", layout="wide")

# Load Assets
IMG= Image.open("images/Clark.jpg")

#----------------------------------------------------------- #divider

st.title("Welcome to Clark's Website")


column1, column2, column3 = st.columns(3)

with column1:
    st.write("Autobiography")
    st.write("""Clark Justin B. Deliupa, an 18-year-old from the Island of Siargao, is a young visionary with a passion for bringing stories to life through the lens of his camera.

Born on April 22 2005, Clark discovered his love for visual storytelling at an early age. Growing up surrounded by the natural beauty of Siargao, he found inspiration in the picturesque landscapes and vibrant local culture. It was here that Clark's journey into the world of creativity began.

From the moment he picked up his first camera, Clark's affinity for creating and editing videos became evident. His unique perspective and technical prowess quickly set him apart, and he became known for his ability to capture the essence of a moment with precision and artistry.

Beyond the digital realm, Clark is also an accomplished artist, channeling his creativity into various forms of visual expression. His love for the arts extends to photography, where he skillfully freezes moments in time, allowing viewers to experience the emotions and beauty of the scenes he captures.

The Island of Siargao, with its azure waters and lush landscapes, serves as both Clark's muse and canvas. His travels, often documented through his lens, showcase not only his adventurous spirit but also the rich tapestry of cultures and landscapes he encounters.

When he's not immersed in the world of visuals, Clark indulges in the joy of discovery through travel. Exploring new places and experiencing diverse cultures fuel his creativity and broaden his perspective on life.""")
    
with column2:
    st.write("")

with column3:
    st.image(IMG)

st.write("Contacts:")

st.markdown("""Facebook:https://www.facebook.com/clarkjustin.clark?mibextid=LQQJ4d""")
