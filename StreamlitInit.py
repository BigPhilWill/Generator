import streamlit as st
import random

# Define the functions to generate random elements for each category
def generate_compliment():
    compliments = ["You're amazing!", "You're beautiful inside and out!", "You're one of a kind!"]
    return random.choice(compliments)

def generate_backhanded_compliment():
    backhanded_compliments = ["You're almost as smart as you look.", "You're not as annoying as I expected."]
    return random.choice(backhanded_compliments)

def generate_animal_fact():
    animal_facts = ["A group of flamingos is called a 'flamboyance.'", "Octopuses have three hearts."]
    return random.choice(animal_facts)

def generate_chat_up_line():
    chat_up_lines = ["Are you a magician? Because whenever I look at you, everyone else disappears.", "Is your name Google? Because you have everything I've been searching for."]
    return random.choice(chat_up_lines)

def generate_famous_quote():
    famous_quotes = ["The only way to do great work is to love what you do. - Steve Jobs", "The only thing we have to fear is fear itself. - Franklin D. Roosevelt"]
    return random.choice(famous_quotes)

# Create the Streamlit app
st.title("Random Generator App")
category = st.sidebar.selectbox("Select a category:", ["Compliment Generator", "Backhanded Compliment Generator", "Animal Fact Generator", "Chat Up Line Generator", "Famous Quote Generator"])

if category == "Compliment Generator":
    st.header(category)
    if st.button("Generate Compliment"):
        st.write(generate_compliment())
elif category == "Backhanded Compliment Generator":
    st.header(category)
    if st.button("Generate Backhanded Compliment"):
        st.write(generate_backhanded_compliment())
elif category == "Animal Fact Generator":
    st.header(category)
    if st.button("Generate Animal Fact"):
        st.write(generate_animal_fact())
elif category == "Chat Up Line Generator":
    st.header(category)
    if st.button("Generate Chat Up Line"):
        st.write(generate_chat_up_line())
elif category == "Famous Quote Generator":
    st.header(category)
    if st.button("Generate Famous Quote"):
        st.write(generate_famous_quote())
