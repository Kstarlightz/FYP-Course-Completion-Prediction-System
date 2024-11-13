import streamlit as st
import joblib

def cc(course):
    if course == "Health": 
        return 1
    elif course == "Arts":
        return 2
    elif course == "Science":
        return 3
    elif course == "Programming":
        return 4
    elif course == "Business":
        return 5
    return None  # Return None if no match is found

def dt(device):
    if device == "Desktop":
        return 0
    elif device == "Mobile":
        return 1
    return None  # Return None if no match is found

st.markdown(
    """
    <style>
    .title-border {
        background-color: #f0f2f6;
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
    <div class="title-border">
        ✅ Course Completion Prediction System 📚
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
        """<style>
    div[class*="stSelectbox"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 20px;
        font-weight: bold;
    }
        </style>
        """, unsafe_allow_html=True)

st.markdown(
        """<style>
    div[class*="stSlider"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 20px;
        font-weight: bold;
    }
        </style>
        """, unsafe_allow_html=True)

st.markdown(
        """<style>
    div[class*="stNumberInput"] > label > div[data-testid="stMarkdownContainer"] > p {
        font-size: 20px;
        font-weight: bold;
    }
        </style>
        """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .prediction-border {
        background-color: #fff3f3;  /* Light red for incomplete */
        border: 2px solid #f44336; /* Red border */
        border-radius: 10px;
        padding: 10px;
        margin-top: 20px;
        font-size: 18px;
        color: #f44336;
        text-align: center;
        font-weight: bold;
    }
    .prediction-border-complete {
        background-color: #e6f7e6;  /* Light green for complete */
        border: 2px solid #4CAF50;  /* Green border */
        border-radius: 10px;
        padding: 10px;
        margin-top: 20px;
        font-size: 18px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Course Category
course=st.selectbox("Course Category:", 
                    ("Business", "Health","Programming","Science","Arts"))

#Device Type                
device=st.selectbox("Device Type:", 
                    ("Desktop","Mobile"))

st.divider() 

# NumberofVideowatched
NumberofVideowatched= st.slider("How many videos have you watched?", 0, 20,0)
st.write('Total Video Watched:' ,NumberofVideowatched)

st.divider() 

# NumberofQuizzTaken
NumberofQuizzTaken= st.slider("How many quizzes have you taken?", 0, 10,0)
st.write('Total Quizzes Taken:' ,NumberofQuizzTaken)

st.divider() 

# Timespentoncourse
Timespentoncourse = st.number_input("How many hours did you spend on the course?"
                       , value=None, placeholder="Type a number...")
st.write("Total time spent: ", Timespentoncourse)

st.divider() 

# QuizScore
score = st.number_input("Insert your quizz score" 
                        , value=None, placeholder="Type a number...")
st.write("Average Score:", score)

st.divider() 

# CompletionRate
rate = st.number_input("What percentage of the course content have you completed?"
                       , value=None, placeholder="Type a number...")
st.write("Percentage Completed:", rate)

st.divider() 

predict=st.button("Predict", type="primary")
if predict:
    result = st.empty()
    result.markdown("Calculating...")

    sc = joblib.load('scaler.pkl')
    new_model = joblib.load('RF_tuning.pkl')
    CourseCategory = cc(course)
    DeviceType = dt(device)
    x=[CourseCategory, Timespentoncourse, NumberofVideowatched, NumberofQuizzTaken, score, rate, DeviceType]
    x=[x]
    new_data_scaled = sc.transform(x)
    prediction = new_model.predict(new_data_scaled)

    if prediction == 0:
        result.markdown(
            '<div class="prediction-border">Most likely won’t complete the course.</div>',
            unsafe_allow_html=True
    )
    else:
        result.markdown(
            '<div class="prediction-border-complete">Most likely to complete the course.</div>',
            unsafe_allow_html=True
    )







