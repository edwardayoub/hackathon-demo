import streamlit as st
import pandas as pd

def main():
    st.title("Hackathon Agenda")

    st.header("Day 1: Presentations, Training, and Setup")
    data_day1 = {
        "Time": [
            "8:00 - 9:00 AM", "9:00 AM - 1:00 PM", "1:00 - 2:00 PM", "2:00 - 3:30 PM", "3:30 - 4:00 PM", "4:00 PM - Evening"
        ],
        "Activity": [
            "Breakfast and Opening Remarks", "Tutorial Sessions (Led by experts)", "Lunch", "Keynote Speech and Problem Explanation",
            "Preliminary Team Findings", "Hackathon Kickoff"
        ],
        "Location": [
            "First Floor, TMC3 Retail Space", "First Floor, TMC3 Retail Space", "First Floor, TMC3 Retail Space", "First Floor, TMC3 Retail Space",
            "First Floor, TMC3 Retail Space", "Second Floor Workspace or First Floor, TMC3 Retail Space"
        ]
    }

    st.subheader("Day 1 Agenda")
    df_day1 = pd.DataFrame(data_day1)
    st.table(df_day1)

    st.header("Day 2: Hackathon and Presentations")
    data_day2 = {
        "Time": [
            "Early Morning - 1:00 PM", "1:00 - 2:00 PM", "2:00 - 4:00 PM", "4:00 - 8:00 PM"
        ],
        "Activity": [
            "Hackathon Continues", "Lunch", "Hackathon Concludes", "Team Presentations, Awards, and Reception Dinner"
        ],
        "Location": [
            "Second Floor Workspace", "TMC3 Atrium", "Second Floor Workspace", "TMC3 Atrium"
        ]
    }

    st.subheader("Day 2 Agenda")
    df_day2 = pd.DataFrame(data_day2)
    st.table(df_day2)

if __name__ == "__main__":
    main()
