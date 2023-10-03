# Copimport numpy as np
import matplotlib.pyplot as plt
import streamlit as st
 
# Header
st.header('Nugroho :sparkles:')
st.subheader('Plot')
 
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Generating x values from -2*pi to 2*pi
y = np.sin(x)  # Calculating sin(x) values
z = np.cos(x)  # Calculating sin(x) values
 
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b')  # Plotting sin(x) curve
ax.plot(x, z, label='cos(x)', color='g')  # Plotting sin(x) curve
ax.set_ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)
 
# subheader
st.subheader("Plot Sin & Cos")
 
col1, col2 = st.columns(2)
 
with col1:
    st.caption('Sin')
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Generating x values from -2*pi to 2*pi
    y = np.sin(x)  # Calculating sin(x) values
 
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(x, y, label='sin(x)', color='b')  # Plotting sin(x) curve
    ax.set_ylabel("Sin x")
    ax.set_xlabel("x")
    ax.tick_params(axis='y', labelsize=20)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
    ax.tick_params(axis='x', labelsize=15)
 
    st.pyplot(fig)
 
with col2:
    st.caption('Cos')
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Generating x values from -2*pi to 2*pi
    y = np.cos(x)  # Calculating sin(x) values
 
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(x, y, label='cos(x)', color='g')  # Plotting cos(x) curve
    ax.set_ylabel("Cos x")
    ax.set_xlabel("x")
    ax.tick_params(axis='y', labelsize=20)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
    ax.tick_params(axis='x', labelsize=15)
 
    st.pyplot(fig0)ghg
              
    
yright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Streamlit! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### See more complex demos
        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
