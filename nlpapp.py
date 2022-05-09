#! python3

import streamlit as st

st.title("Once upon a time")
st.subheader("This is a web app to summarize and translate Grimm's fairy tales")
st.caption("You can choose your favorite fairy tale and the app will summerize it for you into a few lines in whatevere language you want.")

option = st.selectbox("Which fairytale you want to summarize?", 
                      ("Little Snow White", "The Ugly Duckling", "Aladdin and the Wonderful Lamp", "The Sleeping Beauty", "Puss-in-Boots", "Adventures of Tom Thumb", "The Three Bears", "The Little Match Girl", "Beauty and the Beast", "The Story of Cinderella", "Jack the Giant Killer", "Jack and the Beanstalk", "Dick Whittington and His Cat", "The Story of Bluebeard", "Little Red Riding-Hood", "Sindbad the Sailor", "Hansel and Gretel", "The Goose Girl"))
st.write("You selected: ", option)
