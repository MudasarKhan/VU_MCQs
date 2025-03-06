import streamlit as st
import sqlite3
import streamlit as st
from PIL import Image
file_path = r"C:\Users\FFC MM\Desktop\Dashboard_Project\pythonProject\Logo.PNG"
try:
    logo = Image.open(file_path)
    st.sidebar.image(logo, use_column_width=True)
except FileNotFoundError:
    st.error(f"File '{file_path}' Path Dont Find.")
connection = sqlite3.connect("MCQs_Web_Database.db")
cursor = connection.cursor()
st.title("Cyber Village :orange[Virtual-Academy]")
choice = st.selectbox('Login  Or Signup', ['Login', 'Signup'])
if choice == 'Signup':
    with st.form(key="Submit",  clear_on_submit=True):
        st.title("Signup :violet[Form]")
        User_Name = st.text_input("Enter Your Name")
        #Countries List
        countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia",
                     "Austria", "Azerbaijan",
                     "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
                     "Bolivia",
                     "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
                     "Cabo Verde", "Cambodia",
                     "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros",
                     "Congo", "Costa Rica",
                     "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica",
                     "Dominican Republic", "Ecuador", "Egypt",
                     "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji",
                     "Finland", "France", "Gabon",
                     "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
                     "Guinea-Bissau", "Guyana", "Haiti",
                     "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
                     "Italy", "Jamaica", "Japan",
                     "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
                     "Lesotho", "Liberia",
                     "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
                     "Maldives", "Mali", "Malta",
                     "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
                     "Mongolia", "Montenegro",
                     "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand",
                     "Nicaragua", "Niger",
                     "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine",
                     "Panama", "Papua New Guinea",
                     "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda",
                     "Saint Kitts and Nevis",
                     "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
                     "Saudi Arabia", "Senegal",
                     "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
                     "Somalia", "South Africa",
                     "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
                     "Syria", "Taiwan",
                     "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
                     "Tunisia", "Turkey",
                     "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
                     "United States", "Uruguay",
                     "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
        User_Country = st.selectbox("Select Your Country", countries)
        User_DateofBirth = st.date_input("Enter Signup Date")
        User_Gmail = st.text_input("Enter Your Gmail")
        User_Password = st.text_input("Enter Your Password", type='password')
        Submit = st.form_submit_button(label="Submit")
    if Submit:
        cursor.execute(f"INSERT INTO MCQS_Web_Table(User_Name, User_Country, User_DateofBirth, User_Gmail, User_Password) VALUES(?,?,?,?,?)",(User_Name, User_Country, User_DateofBirth, User_Gmail, User_Password))
        connection.commit()
        st.success("Registration Successful Login Now")
if choice == 'Login':
    with st.form(key="Login", clear_on_submit=True):
        st.title("Login :blue[Form]")
        User_Gmail = st.text_input("Enter Your Gmail", key="login_email")
        User_Password = st.text_input("Enter Your Password", type='password', key="login_password")
        Login = st.form_submit_button(label="Login")
        if Login:
            cursor.execute("SELECT * FROM MCQS_Web_Table WHERE User_Gmail=? AND User_Password=?",
                           (User_Gmail, User_Password))
            fetch_User = cursor.fetchone()
            if fetch_User:
                st.success("Login Successful")
                st.markdown(f'<a href="http://localhost:8501/" target="_self">Go to Dashboard</a>', unsafe_allow_html=True)
            else:
                st.error("Login Failed. Please check your credentials")
connection.close()