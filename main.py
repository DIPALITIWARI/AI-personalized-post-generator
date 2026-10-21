import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
def main():
    st.title("LinkedIn Post Generator") 
    col1,col2,col3= st.columns(3)
    fs= FewShotPosts()
    with col1:
        selected_tag=st.selectbox("Select Post Tag",list(fs.unique_tags))
    with col2:
        selected_length=st.selectbox("Select Post Length",["short","medium","long"])
    with col3:
        selected_language=st.selectbox("Select Post Language",["english","hinglish"])
    if st.button("Generate Post"):
        generated_post=generate_post(selected_length,selected_language,selected_tag)
        st.write(generated_post)
if __name__ == "__main__":
   main()