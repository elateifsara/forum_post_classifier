import streamlit as st

import model

def predict(post):
    """
    Predict the category of the post.
    """
    return model.predict(post)

st.title('Post forum Classifier')

st.write("""
        Enter the title and the body of your post. The machine learning model
        will then try to classify your post into one of the 11 categories from
        the amazon e-commerce forum from the DiscourseHub community. 
         """)

post_title = st.text_input('Enter your post title')
post_body = st.text_area('Enter your post body/content', height=400)

post = post_title + ' ' + post_body

submit = st.button('Predict')
if submit:
    prediction = predict(post)
    if prediction :
        st.subheader('Classification Results')
        st.write('Your forum post falls in the ', prediction, 'category of the DiscourseHub Amazon E-commerce forum.')
