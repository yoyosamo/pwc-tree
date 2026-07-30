import streamlit as st
import requests
from st_supabase_connection import SupabaseConnection, execute_query

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
db = st.connection(
    name="supabase",
    type=SupabaseConnection,
    ttl=None,
)

# Perform query.
rows = execute_query(
    db.table("pwc").select("*"),
    ttl="15m",
)

# Print results.
for row in rows.data:
    st.write(row)