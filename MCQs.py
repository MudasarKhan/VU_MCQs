import streamlit as st
from PIL import Image
file_path = r"Logo.PNG"
try:
    logo = Image.open(file_path)
    st.sidebar.image(logo, use_column_width=True)
except FileNotFoundError:
    st.error(f"File '{file_path}' Path Dont Find.")
choice = st.selectbox('Subjects', ['Python', 'Mathematics', 'English', 'Physics', 'Chemistry'])
if choice == 'Mathematics':
    st.title('Math Quiz')
    questions = [
        {"question": "What is the value of π (pi)?", "options": ['3.14', '2.71', '1.62', '4.20'], "answer": "3.14"},
        {"question": "Solve for x: 2x + 3 = 7", "options": ['x = 1', 'x = 2', 'x = 3', 'x = 4'], "answer": "x = 2"},
        {"question": "What is the square root of 16?", "options": ['2', '4', '6', '8'], "answer": "4"},
        {"question": "What is the result of 9 * 9?", "options": ['81', '72', '90', '99'], "answer": "81"},
        {"question": "What is the sum of angles in a triangle?", "options": ['90°', '180°', '270°', '360°'],
         "answer": "180°"},
        {"question": "What is the derivative of x^2?", "options": ['x', '2x', 'x^2', '2'], "answer": "2x"},
        {"question": "Solve for y: y/2 = 6", "options": ['y = 3', 'y = 6', 'y = 12', 'y = 18'], "answer": "y = 12"},
        {"question": "What is the value of the golden ratio?", "options": ['1.41', '1.61', '1.73', '2.23'],
         "answer": "1.61"},
        {"question": "What is the result of 7 + 8?", "options": ['14', '15', '16', '17'], "answer": "15"},
        {"question": "What is the integral of 1/x?", "options": ['ln(x)', 'e^x', 'x', '1/x^2'], "answer": "ln(x)"},
        {"question": "What is the hypotenuse of a right triangle with sides 3 and 4?", "options": ['5', '6', '7', '8'],
         "answer": "5"},
        {"question": "What is the factorial of 5?", "options": ['120', '60', '20', '10'], "answer": "120"},
        {"question": "Solve for z: 3z - 4 = 8", "options": ['z = 2', 'z = 4', 'z = 6', 'z = 8'], "answer": "z = 4"},
        {"question": "What is the perimeter of a square with side length 4?", "options": ['8', '12', '16', '20'],
         "answer": "16"},
        {"question": "What is the area of a circle with radius 3?", "options": ['6π', '9π', '12π', '18π'],
         "answer": "9π"},
        {"question": "What is the cube root of 27?", "options": ['2', '3', '4', '5'], "answer": "3"},
        {"question": "What is the value of 2^5?", "options": ['10', '16', '32', '64'], "answer": "32"},
        {"question": "What is the slope of the line y = 2x + 3?", "options": ['2', '3', '4', '5'], "answer": "2"},
        {"question": "What is the volume of a sphere with radius 2?",
         "options": ['(4/3)π', '(8/3)π', '(16/3)π', '(32/3)π'], "answer": "(32/3)π"},
        {"question": "What is the GCD (Greatest Common Divisor) of 54 and 24?", "options": ['6', '9', '12', '18'],
         "answer": "6"},
    ]

    for i, q in enumerate(questions):
        with st.form(key=f"Form{i}"):
            st.markdown(f" Question {i + 1}: {q['question']}")
            answer = st.radio(f"Options for Question {i + 1}", q['options'], key=f'q{i}')
            submit = st.form_submit_button("Submit Answer 🚀")

            if submit:
                if answer == q['answer']:
                    st.success(f"Correct Answer! 🏆")
                else:
                    st.warning(f"Wrong Answer! ❌")
            st.markdown("<hr style='border:2px solid purple'>", unsafe_allow_html=True)
if choice == 'Python':
        st.title('Python Quiz')
        questions = [
            {"question": "Is Python programming case sensitive? 🤔", "options": ['Yes', 'No'], "answer": "Yes"},
            {"question": "Which keyword is used to create a function in Python?",
             "options": ['def', 'function', 'func', 'lambda'], "answer": "def"},
            {"question": "What does the `len()` function do?",
             "options": ['Returns the length of an object', 'Creates an object', 'Deletes an object', 'None of the above'],
             "answer": "Returns the length of an object"},
            {"question": "Which data type is used to store a sequence of characters?",
             "options": ['int', 'str', 'list', 'tuple'], "answer": "str"},
            {"question": "How do you comment a single line in Python?", "options": ['//', '#', '/*', '<!--'], "answer": "#"},
            {"question": "What is the output of `2 + 2` in Python?", "options": ['4', '22', 'None', 'Error'], "answer": "4"},
            {"question": "Which keyword is used to check if a value exists in a list?",
             "options": ['in', 'exists', 'check', 'find'], "answer": "in"},
            {"question": "How do you start a for loop in Python?",
             "options": ['for i in range():', 'for(i=0; i<10; i++):', 'foreach i in range():', 'for i to 10:'],
             "answer": "for i in range():"},
            {"question": "Which of the following is a mutable data type?", "options": ['tuple', 'list', 'int', 'str'],
             "answer": "list"},
            {"question": "What is the output of `print('Hello, World!'.lower())`?",
             "options": ['Hello, World!', 'hello, world!', 'HELLO, WORLD!', 'None of the above'], "answer": "hello, world!"},
            {"question": "Which module in Python is used to generate random numbers?",
             "options": ['random', 'math', 'numbers', 'os'], "answer": "random"},
            {"question": "What does the `break` statement do?",
             "options": ['Exits the current loop', 'Continues to the next iteration', 'Stops the program', 'None of the above'],
             "answer": "Exits the current loop"},
            {"question": "How do you create a dictionary in Python?",
             "options": ['{key: value}', '[key: value]', '(key, value)', 'None of the above'], "answer": "{key: value}"},
            {"question": "Which function is used to read input from the user?",
             "options": ['input()', 'raw_input()', 'read()', 'scanf()'], "answer": "input()"},
            {"question": "What is the correct way to import a module in Python?",
             "options": ['import module_name', 'include module_name', 'require module_name', 'use module_name'],
             "answer": "import module_name"},
            {"question": "What is the default value returned by a function that doesn't specify a return value?",
             "options": ['0', 'null', 'None', 'undefined'], "answer": "None"},
            {"question": "Which method is used to add an item to the end of a list?",
             "options": ['append()', 'add()', 'insert()', 'push()'], "answer": "append()"},
            {"question": "How do you create a set in Python?",
             "options": ['{1, 2, 3}', '[1, 2, 3]', '(1, 2, 3)', 'None of the above'], "answer": "{1, 2, 3}"},
            {"question": "Which exception is raised when a key is not found in a dictionary?",
             "options": ['KeyError', 'ValueError', 'IndexError', 'TypeError'], "answer": "KeyError"},
            {"question": "How do you convert a string to an integer in Python?",
             "options": ['int()', 'str()', 'float()', 'list()'], "answer": "int()"},
        ]

        for i, q in enumerate(questions):
            with st.form(key=f"Form{i}"):
                st.markdown(f"### Question {i + 1}: {q['question']}")
                answer = st.radio(f"Options for Question {i + 1}", q['options'], key=f'q{i}')
                submit = st.form_submit_button("Submit Answer 🚀")

                if submit:
                    if answer == q['answer']:
                        st.success(f"Correct Answer! 🏆")
                    else:
                        st.warning(f"Wrong Answer! ❌")
                st.markdown("<hr style='border:2px solid violet'>", unsafe_allow_html=True)
if choice == 'English':
    st.title('English Quiz')
    questions_english = [
        {"question": "What is the synonym of 'happy'?", "options": ['Sad', 'Joyful', 'Angry', 'Excited'],
         "answer": "Joyful"},
        {"question": "Choose the correct spelling:", "options": ['Recieve', 'Receive', 'Recive', 'Recieive'],
         "answer": "Receive"},
        {"question": "What is the antonym of 'difficult'?", "options": ['Easy', 'Hard', 'Tough', 'Complicated'],
         "answer": "Easy"},
        {"question": "Complete the proverb: A stitch in time saves ___?", "options": ['Nine', 'Eight', 'Ten', 'Seven'],
         "answer": "Nine"},
        {"question": "Identify the noun in the sentence: 'The cat chased the mouse.'",
         "options": ['Chased', 'Mouse', 'The', 'Cat'], "answer": "Cat"},
        {"question": "Which word means the same as 'rapid'?", "options": ['Slow', 'Quick', 'Dull', 'Heavy'],
         "answer": "Quick"},
        {"question": "Fill in the blank: She is ___ intelligent girl.", "options": ['a', 'an', 'the', 'none'],
         "answer": "an"},
        {"question": "Choose the correct past tense form: 'I ___ to the store yesterday.'",
         "options": ['go', 'went', 'gone', 'going'], "answer": "went"},
        {"question": "What is the plural of 'child'?", "options": ['Childs', 'Children', 'Childes', 'Childrens'],
         "answer": "Children"},
        {"question": "What is the opposite of 'early'?", "options": ['Late', 'Soon', 'Quick', 'Fast'],
         "answer": "Late"},
        {"question": "Choose the correct homophone: 'The wind ___ through the trees.'",
         "options": ['blue', 'blew', 'blow', 'blown'], "answer": "blew"},
        {"question": "What is the main idea of a paragraph?",
         "options": ['Supporting details', 'Topic sentence', 'Conclusion', 'All of the above'],
         "answer": "Topic sentence"},
        {"question": "What is the synonym of 'small'?", "options": ['Tiny', 'Huge', 'Large', 'Big'], "answer": "Tiny"},
        {"question": "Complete the sentence: She ___ her homework on time.",
         "options": ['finishes', 'finish', 'finished', 'finishing'], "answer": "finished"},
        {"question": "Which word is a verb?", "options": ['Run', 'Quick', 'Blue', 'Beautiful'], "answer": "Run"},
        {"question": "Identify the adjective: 'The quick brown fox jumps over the lazy dog.'",
         "options": ['Quick', 'Fox', 'Jumps', 'Over'], "answer": "Quick"},
        {"question": "What is the opposite of 'easy'?", "options": ['Hard', 'Simple', 'Smooth', 'Soft'],
         "answer": "Hard"},
        {"question": "What is the comparative form of 'good'?", "options": ['Gooder', 'Better', 'Best', 'Goodest'],
         "answer": "Better"},
        {"question": "Fill in the blank: She is as ___ as a cucumber.", "options": ['Cool', 'Hot', 'Warm', 'Cold'],
         "answer": "Cool"},
        {"question": "Choose the correct conjunction: 'I like tea ___ I don't like coffee.'",
         "options": ['and', 'but', 'or', 'so'], "answer": "but"},
    ]
    for i, q in enumerate(questions_english):
        with st.form(key=f"FormE{i}"):
            st.markdown(f"**Question {i + 1}: {q['question']}**")
            answer = st.radio(f"Options for Question {i + 1}", q['options'], key=f'eq{i}')
            submit = st.form_submit_button("Submit Answer 🚀")

            if submit:
                if answer == q['answer']:
                    st.success("Correct Answer! 🏆")
                else:
                    st.warning("Wrong Answer! ❌")
            st.markdown("<hr style='border:2px solid purple'>", unsafe_allow_html=True)
if choice == 'Physics':
    import streamlit as st

    st.title('Physics Quiz')

    questions_physics = [
        {"question": "What is the speed of light?",
         "options": ['3 x 10^8 m/s', '3 x 10^6 m/s', '3 x 10^5 m/s', '3 x 10^7 m/s'], "answer": "3 x 10^8 m/s"},
        {"question": "Who discovered the law of gravity?",
         "options": ['Albert Einstein', 'Isaac Newton', 'Galileo Galilei', 'Marie Curie'], "answer": "Isaac Newton"},
        {"question": "What is the unit of force?", "options": ['Newton', 'Joule', 'Watt', 'Pascal'],
         "answer": "Newton"},
        {"question": "What is the formula for kinetic energy?", "options": ['1/2 mv^2', 'mgh', 'mc^2', 'mv'],
         "answer": "1/2 mv^2"},
        {"question": "What is the charge of an electron?", "options": ['+1', '-1', '0', '+2'], "answer": "-1"},
        {"question": "What is the SI unit of power?", "options": ['Watt', 'Joule', 'Newton', 'Pascal'],
         "answer": "Watt"},
        {"question": "What is the acceleration due to gravity on Earth?",
         "options": ['9.8 m/s^2', '8.9 m/s^2', '10.8 m/s^2', '7.8 m/s^2'], "answer": "9.8 m/s^2"},
        {"question": "What is the formula for Ohm's Law?", "options": ['V = IR', 'P = IV', 'F = ma', 'E = mc^2'],
         "answer": "V = IR"},
        {"question": "What is the unit of electric current?", "options": ['Ampere', 'Volt', 'Ohm', 'Watt'],
         "answer": "Ampere"},
        {"question": "Who is known as the father of modern physics?",
         "options": ['Albert Einstein', 'Isaac Newton', 'Niels Bohr', 'Galileo Galilei'], "answer": "Albert Einstein"},
        {"question": "What is the formula for potential energy?", "options": ['mgh', '1/2 mv^2', 'mc^2', 'mv'],
         "answer": "mgh"},
        {"question": "What is the value of Planck's constant?",
         "options": ['6.626 x 10^-34 Js', '3.00 x 10^8 m/s', '1.60 x 10^-19 C', '9.81 m/s^2'],
         "answer": "6.626 x 10^-34 Js"},
        {"question": "What is the unit of frequency?", "options": ['Hertz', 'Joule', 'Newton', 'Pascal'],
         "answer": "Hertz"},
        {"question": "What is the formula for momentum?", "options": ['mv', 'mgh', 'mc^2', '1/2 mv^2'], "answer": "mv"},
        {"question": "What is the value of absolute zero in Celsius?",
         "options": ['-273.15°C', '-100°C', '-273°C', '0°C'], "answer": "-273.15°C"},
        {"question": "What is the unit of pressure?", "options": ['Pascal', 'Watt', 'Newton', 'Joule'],
         "answer": "Pascal"},
        {"question": "What is the formula for work done?", "options": ['W = Fd', 'E = mc^2', 'P = IV', 'V = IR'],
         "answer": "W = Fd"},
        {"question": "What is the value of gravitational constant (G)?",
         "options": ['6.674 x 10^-11 N m^2/kg^2', '9.81 m/s^2', '1.60 x 10^-19 C', '3.00 x 10^8 m/s'],
         "answer": "6.674 x 10^-11 N m^2/kg^2"},
        {"question": "What is the formula for wave speed?", "options": ['v = fλ', 'E = mc^2', 'F = ma', 'V = IR'],
         "answer": "v = fλ"},
        {"question": "Who formulated the theory of relativity?",
         "options": ['Albert Einstein', 'Isaac Newton', 'Niels Bohr', 'Galileo Galilei'], "answer": "Albert Einstein"},
    ]
    for i, q in enumerate(questions_physics):
        with st.form(key=f"FormP{i}"):
            st.markdown(f"**Question {i + 1}: {q['question']}**")
            answer = st.radio(f"Options for Question {i + 1}", q['options'], key=f'pq{i}')
            submit = st.form_submit_button("Submit Answer 🚀")

            if submit:
                if answer == q['answer']:
                    st.success("Correct Answer! 🏆")
                else:
                    st.warning("Wrong Answer! ❌")
            st.markdown("<hr style='border:2px solid purple'>", unsafe_allow_html=True)
if choice == 'Chemistry':
    st.title('Chemistry Quiz')
    questions_chemistry = [
        {"question": "What is the chemical symbol for water?", "options": ['H2O', 'O2', 'H2', 'OH'], "answer": "H2O"},
        {"question": "Who is known as the father of modern chemistry?",
         "options": ['Isaac Newton', 'Albert Einstein', 'Antoine Lavoisier', 'Marie Curie'],
         "answer": "Antoine Lavoisier"},
        {"question": "What is the atomic number of Carbon?", "options": ['6', '8', '12', '14'], "answer": "6"},
        {"question": "What is the pH of pure water?", "options": ['7', '5', '3', '10'], "answer": "7"},
        {"question": "What is the chemical formula for table salt?", "options": ['NaCl', 'KCl', 'NaOH', 'HCl'],
         "answer": "NaCl"},
        {"question": "What is the most abundant gas in Earth's atmosphere?",
         "options": ['Oxygen', 'Hydrogen', 'Nitrogen', 'Carbon Dioxide'], "answer": "Nitrogen"},
        {"question": "What is the chemical symbol for Gold?", "options": ['Ag', 'Au', 'Gd', 'Pb'], "answer": "Au"},
        {"question": "What is the main constituent of natural gas?",
         "options": ['Methane', 'Ethane', 'Propane', 'Butane'], "answer": "Methane"},
        {"question": "What is the atomic mass of Oxygen?", "options": ['8', '16', '18', '32'], "answer": "16"},
        {"question": "What is the name of the element with the symbol 'Fe'?",
         "options": ['Iron', 'Copper', 'Lead', 'Zinc'], "answer": "Iron"},
        {"question": "What is the chemical formula for ammonia?", "options": ['NH3', 'NH4', 'N2H4', 'N2O'],
         "answer": "NH3"},
        {"question": "Who discovered the electron?",
         "options": ['Isaac Newton', 'Niels Bohr', 'J.J. Thomson', 'Ernest Rutherford'], "answer": "J.J. Thomson"},
        {"question": "What is the chemical formula for sulfuric acid?", "options": ['H2SO4', 'HCl', 'H2O', 'HNO3'],
         "answer": "H2SO4"},
        {"question": "What is the process of converting liquid to gas called?",
         "options": ['Sublimation', 'Condensation', 'Evaporation', 'Melting'], "answer": "Evaporation"},
        {"question": "What is the chemical formula for methane?", "options": ['CH4', 'C2H6', 'C3H8', 'C4H10'],
         "answer": "CH4"},
        {"question": "What is the atomic number of Helium?", "options": ['1', '2', '4', '10'], "answer": "2"},
        {"question": "What is the symbol for the element Potassium?", "options": ['K', 'P', 'Pt', 'Po'], "answer": "K"},
        {"question": "What is the name of the first element on the periodic table?",
         "options": ['Helium', 'Lithium', 'Hydrogen', 'Oxygen'], "answer": "Hydrogen"},
        {"question": "What is the chemical formula for baking soda?", "options": ['NaHCO3', 'Na2CO3', 'NaCl', 'KOH'],
         "answer": "NaHCO3"},
        {"question": "What is the term for a substance that speeds up a chemical reaction?",
         "options": ['Catalyst', 'Inhibitor', 'Reactant', 'Product'], "answer": "Catalyst"},
    ]

    for i, q in enumerate(questions_chemistry):
        with st.form(key=f"FormC{i}"):
            st.markdown(f"**Question {i + 1}: {q['question']}**")
            answer = st.radio(f"Options for Question {i + 1}", q['options'], key=f'cq{i}')
            submit = st.form_submit_button("Submit Answer 🚀")

            if submit:
                if answer == q['answer']:
                    st.success("Correct Answer! 🏆")
                else:
                    st.warning("Wrong Answer! ❌")
            st.markdown("<hr style='border:2px solid purple'>", unsafe_allow_html=True)


