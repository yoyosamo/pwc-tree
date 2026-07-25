import streamlit as st

u = 'https://committees-api.parliament.sa.gov.au/api/CommitteePublicFolder'

p = {
    'committeeId':'451'
}


st.title("PWC Tree")

response = requests.get(u, params=p)
data = response.json()

d = data['Folders']

st.write("Done")
st.write(d)
