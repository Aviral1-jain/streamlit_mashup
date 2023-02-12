import streamlit as st
import os
import sys
import io
import subprocess

#### GLOBAL VARIABLES ####

gmail = "bluesmurf20013@gmail.com"
gmailpwd = "jteccqnsionjlzwa"

#### MAIN PAGE ####

st.header('Mashup Project')

email = st.text_input("Enter your email: ")
singerName = st.text_input("Enter singer name: ")
songNumber = st.text_input("Enter number of songs: ")
songDuration = st.text_input("Enter each song duration(seconds)")
outputName = st.text_input("Enter output file name: ")

flag = 0
if st.button("Submit"):
    flag = 1

st.write("\nLOGS:\n")

if flag == 1:
    st.write("Creating Mashup")
    subprocess.call(["python", "assign6.py", singerName, str(songNumber), str(songDuration), outputName, email])
    st.write("Mashup Completed")
else:
    st.write("")