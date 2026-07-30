import streamlit as st
import requests
from st_supabase_connection import SupabaseConnection

u = 'https://committees-api.parliament.sa.gov.au/api/CommitteePublicFolder'

p = {
    'committeeId':'451'
}


st.title("PWC Tree")

response = requests.get(u, params=p)
data = response.json()

d = data['Folders']

st.write("Done")
# st.write(d)

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="pwc", ttl="10m").execute()

# Print results.
for row in rows.data:
    st.write(row)