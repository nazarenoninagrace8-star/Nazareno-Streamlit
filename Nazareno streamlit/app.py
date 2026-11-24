
import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Niña Grace Nazareno | Multi-Tool App",
    page_icon="🛠️",
    layout="wide"
)

# ==========================================
# 2. HEADER
# ==========================================

st.header("Niña Grace Nazareno")

st.title("🛠️ Multi-Tool Web Application")

st.caption(
    "A simple and interactive web application "
    "developed using Python and Streamlit."
)

st.divider()

# ==========================================
# 3. NAVIGATION BAR
# ==========================================

page = st.radio(
    "Navigation Menu",
    ["Home", "Calculator", "Unit Converter", "About"],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# ==========================================
# 4. HOME PAGE
# ==========================================

if page == "Home":

    st.title("🏠 Home Page")

    st.subheader("Welcome to My Multi-Tool Application!")

    st.write("""
    This application provides simple and useful tools
    for mathematical calculations and unit conversions.

    ### Available Features

    - 🧮 Basic Calculator
    - 📏 Unit Converter
    - 📊 Numerical Data Preview
    - ℹ️ Application Information

    Select a tool from the navigation bar above.
    """)

    st.success("Welcome! Your application is ready to use.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧮 Calculator")
        st.write(
            "Perform basic mathematical operations "
            "quickly and easily."
        )

    with col2:
        st.subheader("📏 Unit Converter")
        st.write(
            "Convert different measurements "
            "from one unit to another."
        )

    st.divider()

    st.subheader("📊 Python Libraries Used")

    library_data = pd.DataFrame({
        "Library": ["Streamlit", "Pandas", "NumPy"],
        "Purpose": [
            "Building the web application",
            "Organizing and displaying data",
            "Performing numerical calculations"
        ]
    })

    st.dataframe(
        library_data,
        use_container_width=True,
        hide_index=True
    )

# ==========================================
# 5. CALCULATOR
# ==========================================

elif page == "Calculator":

    st.title("🧮 Basic Calculator")

    st.write("Enter two numbers and select an operation.")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input(
            "First Number",
            value=0.0,
            key="num1"
        )

    with col2:
        num2 = st.number_input(
            "Second Number",
            value=0.0,
            key="num2"
        )

    operation = st.selectbox(
        "Select Mathematical Operation",
        [
            "Addition (+)",
            "Subtraction (-)",
            "Multiplication (×)",
            "Division (÷)",
            "Exponentiation (^)",
            "Modulus (%)"
        ]
    )

    if st.button("Calculate Result"):

        result = None

        if operation == "Addition (+)":
            result = np.add(num1, num2)

        elif operation == "Subtraction (-)":
            result = np.subtract(num1, num2)

        elif operation == "Multiplication (×)":
            result = np.multiply(num1, num2)

        elif operation == "Division (÷)":

            if num2 == 0:
                st.error("Cannot divide by zero!")
            else:
                result = np.divide(num1, num2)

        elif operation == "Exponentiation (^)":
            result = np.power(num1, num2)

        elif operation == "Modulus (%)":

            if num2 == 0:
                st.error("Cannot divide by zero!")
            else:
                result = np.mod(num1, num2)

        if result is not None:
            st.success(f"Result: {result}")

# ==========================================
# 6. UNIT CONVERTER
# ==========================================

elif page == "Unit Converter":

    st.title("📏 Unit Converter")

    st.write("Convert different units of measurement easily.")

    category = st.selectbox(
        "Select Conversion Category",
        [
            "Length",
            "Weight",
            "Temperature",
            "Volume",
            "Time",
            "Speed",
            "Area",
            "Digital Storage"
        ]
    )

    value = st.number_input(
        "Enter Value",
        value=1.0
    )

    # Conversion factors use a common base unit.

    conversion_units = {

        "Length": {
            "Meters": 1,
            "Kilometers": 1000,
            "Centimeters": 0.01,
            "Millimeters": 0.001,
            "Miles": 1609.344,
            "Yards": 0.9144,
            "Feet": 0.3048,
            "Inches": 0.0254
        },

        "Weight": {
            "Kilograms": 1,
            "Grams": 0.001,
            "Milligrams": 0.000001,
            "Metric Tons": 1000,
            "Pounds": 0.45359237,
            "Ounces": 0.028349523125
        },

        "Volume": {
            "Liters": 1,
            "Milliliters": 0.001,
            "Cubic Meters": 1000,
            "Gallons (US)": 3.785411784,
            "Cups (US)": 0.2365882365
        },

        "Time": {
            "Seconds": 1,
            "Minutes": 60,
            "Hours": 3600,
            "Days": 86400,
            "Weeks": 604800
        },

        "Speed": {
            "Meters/Second": 1,
            "Kilometers/Hour": 0.277777778,
            "Miles/Hour": 0.44704,
            "Knots": 0.514444444
        },

        "Area": {
            "Square Meters": 1,
            "Square Kilometers": 1000000,
            "Hectares": 10000,
            "Acres": 4046.8564224,
            "Square Feet": 0.09290304
        },

        "Digital Storage": {
            "Bytes": 1,
            "Kilobytes": 1000,
            "Megabytes": 1000000,
            "Gigabytes": 1000000000,
            "Terabytes": 1000000000000
        }
    }

    # Select available units

    if category == "Temperature":

        units = ["Celsius", "Fahrenheit", "Kelvin"]

    else:

        units = list(conversion_units[category].keys())

    col1, col2 = st.columns(2)

    with col1:
        from_unit = st.selectbox(
            "Convert From",
            units
        )

    with col2:
        to_unit = st.selectbox(
            "Convert To",
            units,
            index=1 if len(units) > 1 else 0
        )

    # Perform conversion

    if st.button("Convert Units"):

        if category == "Temperature":

            # Convert source value to Celsius

            if from_unit == "Celsius":
                base_value = value

            elif from_unit == "Fahrenheit":
                base_value = (value - 32) * 5 / 9

            else:
                base_value = value - 273.15

            # Convert Celsius to target unit

            if to_unit == "Celsius":
                result = base_value

            elif to_unit == "Fahrenheit":
                result = (base_value * 9 / 5) + 32

            else:
                result = base_value + 273.15

        else:

            # Convert using common base unit

            base_value = (
                value * conversion_units[category][from_unit]
            )

            result = (
                base_value / conversion_units[category][to_unit]
            )

        st.success(
            f"{value:g} {from_unit} = {result:.6g} {to_unit}"
        )

        # Display conversion information using Pandas

        conversion_data = pd.DataFrame({
            "Description": ["Original Value", "Converted Value"],
            "Value": [
                f"{value:g} {from_unit}",
                f"{result:.6g} {to_unit}"
            ]
        })

        st.dataframe(
            conversion_data,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    st.caption(
        "Note: Digital storage uses decimal units "
        "(1 KB = 1,000 bytes)."
    )

# ==========================================
# 7. ABOUT PAGE
# ==========================================

elif page == "About":

    st.title("ℹ️ About This Application")

    st.subheader("Application Information")

    st.write("""
    The Multi-Tool Web Application is a simple
    interactive application developed using Python
    and the Streamlit framework.

    It demonstrates basic programming concepts,
    mathematical operations, data handling,
    and interactive web application development.
    """)

    st.divider()

    st.subheader("Technologies Used")

    technologies = pd.DataFrame({
        "Technology": [
            "Python",
            "Streamlit",
            "Pandas",
            "NumPy"
        ],
        "Description": [
            "Main programming language",
            "Web application framework",
            "Data organization and manipulation",
            "Numerical computations"
        ]
    })

    st.dataframe(
        technologies,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Developer Information")

    st.write("**Developer:** Niña Grace Nazareno")
    st.write("**Subject:** BES212")
    st.write("**Project:** Multi-Tool Web Application")

    st.success("Thank you for using my application!")

# ==========================================
# 8. FOOTER
# ==========================================

st.divider()

st.caption(
    "Developed by Niña Grace Nazareno | "
    "Powered by Python, Streamlit, Pandas, and NumPy"
)
