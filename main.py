import streamlit as st 

st.markdown("<h1 style='font-size:55px;''> Unit Converter</h1>",unsafe_allow_html=True)

st.markdown("<h2 style='font-size:24px;'>Choose a category:</h2>", unsafe_allow_html=True)

categories = st.radio('' ,  ['📦 Volume','📏 Length', '⚖️ Weight', '🌡️ Temprature',' 🕒Time' ], horizontal=True)

if categories == '📏 Length':
    units = ['Meters','Kilometers','Feet','Miles','Centimeters']
elif categories == '⚖️ Weight':
    units = ['Kilograms' , 'Grams', 'Ounces','Pounds']
elif categories ==  '🌡️ Temprature':
    units = ['Farenhite', 'Celsius', 'Kelvin']
elif categories == ' 🕒Time' :
    units = ['Seconds', 'Minutes','Hours','Days']
elif categories == '📦 Volume':
    units =['Liters', 'Milliliters', 'Gallons']

else:
   st.error('please enter valid number')


# input from user

value = st.number_input('Enter Value :' ,min_value=0.00 , format='%.2f')

def converter(value, unit_from , unit_to):

    convesions ={

    "Liters": {"Milliliters": value * 1000,  "Gallons": value * 0.264172},
    "Milliliters": {"Liters": value / 1000, "Gallons": value * 0.000264172},
    "Gallons": {"Liters": value / 0.264172, "Milliliters": value / 0.000264172,},

    "Meters": {"Kilometers": value / 1000, "Miles": value * 0.000621371, "Feet": value * 3.28084,'Centimeters':value * 100},
    "Kilometers": {"Meters": value * 1000, "Miles": value * 0.621371, "Feet": value * 3280.84 ,'Centimeters':value * 100},  
    "Feet": {"Meters": value / 3.28084, "Kilometers": value / 3280.84, "Miles": value * 0.000189394 ,'Centimeters':value * 100},  
    'Centimeters':{"Kilometers": value / 1000, "Miles": value * 0.000621371, "Feet": value * 3.28084,"Meters": value / 3.28084, },

    "Kilograms": {"Grams": value * 1000, "Pounds": value * 2.20462, "Ounces": value * 35.274},
    "Grams": {"Kilograms": value / 1000, "Pounds": value * 0.00220462, "Ounces": value * 0.035274},
    "Pounds": {"Kilograms": value / 2.20462, "Grams": value * 453.592, "Ounces": value * 16},  

    "Celsius": {"Fahrenheit": (value * 9/5) + 32, "Kelvin": value + 273.15},
    "Fahrenheit": {"Celsius": (value - 32) * 5/9, "Kelvin": ((value - 32) * 5/9) + 273.15},
    "Kelvin": {"Celsius": value - 273.15, "Fahrenheit": ((value - 273.15) * 9/5) + 32},

    "Seconds": {"Minutes": value / 60, "Hours": value / 3600, "Days": value / 86400},
    "Minutes": {"Seconds": value * 60, "Hours": value / 60, "Days": value / 1440},
    "Hours": {"Seconds": value * 3600, "Minutes": value * 60, "Days": value / 24},
    "Days": {"Seconds": value * 86400, "Minutes": value * 1440, "Hours": value * 24}

}
    return convesions.get(unit_from ,{}).get(unit_to,'invalid Conversion')



# Dropdowns for "From" & "To" Units 

unit_from = st.selectbox('from unit:', units)
unit_to =   st.selectbox('to_units:' , units)

st.subheader('Result')

# check both values are not same

if unit_to != unit_from:
    result = converter(value , unit_from, unit_to)
    st.success(f'Converted value: {result} {unit_to}')

else:
    st.warning('Please enter diffrent value')


