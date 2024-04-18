import streamlit as st
import openai

# Define the API key and base URL
OPENAI_API_KEY = "80bc8e21ddb6c068cb1adf347c46ee6aaa487627e2f9416ef9cd5ed81213350c"
OPENAI_BASE_URL = "https://api.together.xyz/v1"

# Create the OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY, base_url=OPENAI_BASE_URL)

# Define the pages
def home():
    st.title("AI - Verse")
    st.subheader("Unleash the Power of Artificial Intelligence")

    # Add a logo
    logo_col1, logo_col2 = st.columns(2)
    with logo_col1:
        st.image("coding.png", width=200)  # Replace "coding.png" with your logo file path

    # Add taglines
    with logo_col2:
        st.write("## AI - Verse")
        st.write("- Empower your code")
        st.write("- Enhance your productivity")
        st.write("- Embrace the future")

    # Add SVG icons for features
    features_col1, features_col2, features_col3, features_col4, features_col5 = st.columns(5)
    with features_col1:
        st.image("coding.png", width=100)  # Replace "coding.png" with your SVG file path
        st.write("Code Explainer")

    with features_col2:
        st.image("coding.png", width=100)
        st.write("Code Generator")

    with features_col3:
        st.image("coding.png", width=100)
        st.write("Code Debugger")

    with features_col4:
        st.image("coding.png", width=100)
        st.write("Code Documentation")

    with features_col5:
        st.image("coding.png", width=100)
        st.write("Code Reviewer")

def code_explainer():
    st.header("Code Explainer")
    code_input = st.text_area("Enter your code here:")

    if st.button("Explain Code"):
        system_content = "You are an AI code explainer. Provide a detailed explanation of the provided code."
        user_content = code_input

        chat_completion = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            temperature=0.7,
            max_tokens=1024,
        )

        response = chat_completion.choices[0].message.content
        st.write("Code Explanation:")
        st.markdown(response)

def code_generator():
    st.header("Code Generator")
    code_input = st.text_area("Enter your code generation input here:")

    if st.button("Generate Code"):
        system_content = ''' markdown
          You are an AI code generator. Generate code based on the provided input.
             '''

        user_content = code_input

        chat_completion = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            temperature=0.7,
            max_tokens=1024,
        )

        generated_code = chat_completion.choices[0].message.content
        st.header("Generated Code:")
        st.markdown(generated_code)

def code_debugger():
    st.header("Code Debugger")
    code_input = st.text_area("Enter your code that needs debugging:")

    if st.button("Debug Code"):
        system_content = "You are an AI code debugger. Identify errors and suggest improvements for the provided code."
        user_content = code_input

        chat_completion = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            temperature=0.7,
            max_tokens=1024,
        )

        debug_results = chat_completion.choices[0].message.content
        st.header("Debugging Results:")
        st.markdown(debug_results)

def code_documentation():
    st.header("Code Documentation")
    code_input = st.text_area("Enter your code for documentation:")

    if st.button("Generate Documentation"):
        system_content = "You are an AI code documenter. Generate documentation for the provided code."
        user_content = code_input

        chat_completion = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            temperature=0.7,
            max_tokens=1024,
        )

        documentation = chat_completion.choices[0].message.content
        st.header("Code Documentation:")
        st.markdown(documentation)

def code_reviewer():
    st.header("Code Reviewer")
    code_input = st.text_area("Enter your code for review:")

    if st.button("Review Code"):
        system_content = "You are an AI code reviewer. Provide feedback and suggestions for the provided code."
        user_content = code_input

        chat_completion = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            temperature=0.7,
            max_tokens=1024,
        )

        review_feedback = chat_completion.choices[0].message.content
        st.header("Code Review Feedback:")
        st.markdown(review_feedback)

def ai_interview():
    st.header("AI Interviewer")

    conversation_history = []

    # Get user's name
    name = st.text_input("What is your name?", key='name_input')
    if name:
        conversation_history.append({"role": "user", "content": name})

    # Get job position
    job_position = st.text_input("What is your job position?", key='job_position_input')
    if job_position:
        conversation_history.append({"role": "user", "content": job_position})

    # Select experience level
    experience_options = ["Fresher", "Student", "Less than 1 year", "1-3 years", "3-5 years", "More than 5 years"]
    experience = st.selectbox("Select your experience level:", experience_options, key='experience_input')
    if experience:
        conversation_history.append({"role": "user", "content": experience})

    # Check if all three fields are filled
    if name and job_position and experience:
        # Start interview
        interview_in_progress = True
        question_count = 0
        while interview_in_progress and question_count < 5:  # Limit to a maximum of 5 questions
            # Generate interview question based on conversation content
            conversation_prompt = "\n".join([msg["content"] for msg in conversation_history if msg["role"] == "user"])

            # Generate interview question using OpenAI
            system_content = "You are an interviewer. Generate an appropriate interview question based on the conversation content."
            user_content = conversation_prompt

            chat_completion = client.chat.completions.create(
                model="mistralai/Mixtral-8x7B-Instruct-v0.1",
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.7,
                max_tokens=1024,
            )

            response = chat_completion.choices[0].message.content
            st.markdown(response)

            # Get user response
            user_response = st.text_input("Your answer:", key=f'answer_input_{question_count}')
            if user_response:
                conversation_history.append({"role": "user", "content": user_response})
                question_count += 1
            else:
                interview_in_progress = False

        # End interview button
        if st.button("End Interview"):
            interview_in_progress = False

        # Generate feedback after the interview ends
        if not interview_in_progress and question_count > 0:
            # Provide interview summary and feedback
            st.subheader("Interview Summary")

            chat_completion = client.chat.completions.create(
                model="mistralai/Mixtral-8x7B-Instruct-v0.1",
                messages=[
                    {"role": "system", "content": '''You are an experienced, empathetic, and personable interviewer. Your goal is to have an engaging and constructive dialogue with the candidate, and to gain genuine insights into their background, skills, and potential fit for the role.

Drawing from the conversation so far, please generate an appropriate interview question that will encourage the candidate to open up and share meaningful information about themselves. Remember to maintain a friendly, supportive, and professional demeanor throughout the interview process. Your aim is to make the candidate feel comfortable and valued, so they can truly showcase their abilities and personality.

Approach this interaction with empathy and a genuine interest in learning more about the candidate as an individual. Your goal is not just to assess their qualifications, but to have a positive and rewarding exchange that leaves them feeling heard and appreciated.

'''},
                    {"role": "user", "content": "\n".join([msg["content"] for msg in conversation_history])},
                ],
                temperature=0.7,
                max_tokens=1024,
            )

            review_feedback = chat_completion.choices[0].message.content
            st.write("Review Feedback:")
            st.markdown(review_feedback)

# Define the pages
pages = {
    "Home": home,
    "Code Explainer": code_explainer,
    "Code Generator": code_generator,
    "Code Debugger": code_debugger,
    "Code Documentation": code_documentation,
    "Code Reviewer": code_reviewer,
    "AI Interviewer": ai_interview,
}

# Set the default page
default_page = "Home"

# Create the sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()), index=list(pages.keys()).index(default_page))

# Run the selected page
pages[selection]()