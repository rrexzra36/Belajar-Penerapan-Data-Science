import streamlit as st
import pandas as pd
import time
from data_preprocessing import *

from prediction import prediction

#Setting page
st.set_page_config(page_title="🎓 Students Performance", layout="wide")

st.markdown("""
    <div style='margin-bottom: 50px; border-radius: 10px; text-align: center;'>
        <h1>✨ JAYA JAYA INSTITUTE ✨</h1>
        <h3>Student's Academic Performance Prediction</h3>
    </div>
""", unsafe_allow_html=True)

# Initialize an empty dictionary to store user input
data = pd.DataFrame()

# Convert user input dictionary to DataFrame
# user_input_df = pd.DataFrame(data, index=[0])

st.markdown("### 🧑‍🎓 Student Information")
col1, col2, col3 = st.columns(3)
with col1:
    encoder_Tuition_fees_up_to_date.fit(['Not Update', 'Update'])
    Tuition_fees_up_to_date = st.selectbox(label='Tuition fees', options=['Not Update', 'Update'], index=1)
    data['Tuition_fees_up_to_date'] = [Tuition_fees_up_to_date]

with col2:
    encoder_Scholarship_holder.fit(['Non Scholarship', 'Scholarship'])
    Scholarship_holder = st.selectbox(label='Scholarship holder', options=['Non Scholarship', 'Scholarship'], index=0)
    data['Scholarship_holder'] = [Scholarship_holder]

with col3:
    encoder_Debtor.fit(['Non Debtor', 'Debtor'])
    Debtor = st.selectbox(label='Debtor', options=['Non Debtor', 'Debtor'], index=1)
    data['Debtor'] = [Debtor]

col4, col5, col6 = st.columns(3)
with col4:
    encoder_Displaced.fit(['Non Displaced', 'Displaced'])
    Displaced = st.selectbox(label='Displaced', options=['Non Displaced', 'Displaced'], index=0)
    data['Displaced'] = [Displaced]

with col5:
    encoder_Daytime_evening_attendance.fit(['Daytime', 'Evening'])
    Daytime_evening_attendance = st.selectbox(label='Attendance', options=['Daytime', 'Evening'], index=0)
    data['Daytime_evening_attendance'] = [Daytime_evening_attendance]

with col6:
    encoder_Gender.fit(['Female', 'Male'])
    Gender = st.selectbox(label='Gender', options=['Female', 'Male'], index=1)
    data['Gender'] = [Gender]

st.markdown("### 📊 Academic Scores")
col7 = st.columns(1)[0]
with col7:
    Admission_grade = st.slider(label='Admission Grade', min_value=0, max_value=200, value=100)
    data['Admission_grade'] = [Admission_grade]

col8 = st.columns(1)[0]
with col8:
    Previous_qualification_grade = st.slider(label='Previous Qualification Grade', min_value=0, max_value=200, value=100)
    data['Previous_qualification_grade'] = [Previous_qualification_grade]

st.markdown("### 📑 Curricular Units 1st Semester")
col9, col10= st.columns(2)
with col9:
    Curricular_units_1st_sem_approved = st.number_input(label='1st Sem Approved', value=5)
    data['Curricular_units_1st_sem_approved'] = [Curricular_units_1st_sem_approved]
with col10:
    Curricular_units_1st_sem_grade = st.number_input(label='1st Sem Grade', value=12)
    data['Curricular_units_1st_sem_grade'] = [Curricular_units_1st_sem_grade]

col11, col12= st.columns(2)
with col11:
    Curricular_units_1st_sem_enrolled = st.number_input(label='1st Sem Enrolled', value=6)
    data['Curricular_units_1st_sem_enrolled'] = [Curricular_units_1st_sem_enrolled]
with col12:
    Curricular_units_1st_sem_credited = st.number_input(label='1st Sem Credited', value=0)
    data['Curricular_units_1st_sem_credited'] = [Curricular_units_1st_sem_credited]

st.markdown("### 📑 Curricular Units 2nd Semester")
col13, col14= st.columns(2)
with col13:
    Curricular_units_2nd_sem_approved = st.number_input(label='2nd Sem Approved', value=5)
    data['Curricular_units_2nd_sem_approved'] = [Curricular_units_2nd_sem_approved]
with col14:
    Curricular_units_2nd_sem_grade = st.number_input(label='2nd Sem Grade', value=12)
    data['Curricular_units_2nd_sem_grade'] = [Curricular_units_2nd_sem_grade]

col15, col16= st.columns(2)
with col15:
    Curricular_units_2nd_sem_enrolled = st.number_input(label='2nd Sem Enrolled', value=6)
    data['Curricular_units_2nd_sem_enrolled'] = [Curricular_units_2nd_sem_enrolled]
with col16:
    Curricular_units_2nd_sem_credited = st.number_input(label='2nd Sem Credited', value=0)
    data['Curricular_units_2nd_sem_credited'] = [Curricular_units_2nd_sem_credited]

# Convert user input dictionary to DataFrame
user_input_df = pd.DataFrame(data, index=[0])

# Display user input
with st.expander("View Raw Dataset"):
        st.dataframe(data=user_input_df, width=1200, height=20)
# Preprocess data and make prediction on button click
if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.spinner("Predicting..."):
        time.sleep(2)  # Simulating prediction process
        # Create a new DataFrame for the processed data
        with st.expander("View Proccessed Dataset"):
            st.dataframe(data=new_data, width=1200, height=20)
        time.sleep(2)  # Simulating prediction process
        output = prediction(new_data)
        st.toast("🎉 Prediction completed!")

        # Display the prediction result
        if output == "Graduate":
            st.balloons()
            result_style = """
            <div style='background-color:#d1e7dd; padding: 30px 20px; border-radius: 12px; margin-top: 30px; text-align: center;'>
            {content}
            </div>
            """
            content = "<h4 style='color:green;'>Congratulations! The student is predicted to graduate successfully! 🎓</h4>"
        elif output == "Dropout":
            st.snow()
            result_style = """
            <div style='background-color:#f8d7da; border-radius: 12px; text-align: center;'>
            {content}
            </div>
            """
            content = "<h4 style='color:red;'>Warning! The student is at risk of dropping out. 🚨</h4>"
        else:
            result_style = """
            <div style='background-color:#fff3cd; border-radius: 12px; text-align: center;'>
            {content}
            </div>
            """
            content = "<h4 style='color:orange;'>The student may need extra support. 📚</h4>"
        st.markdown(result_style.format(content=content), unsafe_allow_html=True)