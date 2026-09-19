import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Lab Growth Visualizer", layout="wide")
st.title("🔬 Universal Bacterial Growth Curve Analyzer")
st.subheader("Drag and drop any lab spreadsheet to visualize data in real-time.")

# 2. Dynamic File Uploader Box
uploaded_file = st.file_uploader(
    "📂 Upload your lab Excel file (.xlsx) or CSV file:", 
    type=["xlsx", "csv"]
)

# 3. Read the Data Only If a File is Uploaded
if uploaded_file is not None:
    try:
        # Automatically detect if it's CSV or Excel
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        st.success("🎉 File uploaded successfully!")
    except Exception as e:
        st.error(f"Error reading the file: {e}")
        st.stop()

    # 4. Sidebar Dynamic Control Panel
    st.sidebar.header("🎛️ Control Panel")
    
    # Get all column options dynamically from the uploaded file
    all_columns = list(df.columns)
    
    # Let the user pick which column represents the X-Axis (e.g., Hour, Time)
    x_axis = st.sidebar.selectbox("Select X-Axis Column (Time):", options=all_columns, index=0)
    
    # Let the user pick multiple numeric columns for the Y-Axis (e.g., Strains, Concentrations)
    remaining_columns = [col for col in all_columns if col != x_axis]
    strain_choice = st.sidebar.multiselect(
        "Select Columns to Plot (Y-Axis):",
        options=remaining_columns,
        default=remaining_columns[:2] if len(remaining_columns) >= 2 else remaining_columns
    )

    # 5. Build Dynamic Layout Columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"### 📈 Interactive Chart ({', '.join(strain_choice)} over {x_axis})")
        if strain_choice:
            st.line_chart(data=df, x=x_axis, y=strain_choice)
        else:
            st.warning("Please select at least one data column to plot in the sidebar.")

    with col2:
        st.markdown("### 📊 Interactive Lab Dataset Grid")
        display_cols = [x_axis] + strain_choice
        st.dataframe(df[display_cols], hide_index=True)

else:
    # Message shown when the dashboard is completely blank/waiting for a file
    st.info("💡 Waiting for a file to be uploaded. You can drag and drop your 'mock_lab_data.xlsx' here to test it!")
