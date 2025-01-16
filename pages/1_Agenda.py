import streamlit as st
import pandas as pd

def main():
    st.title("Hackathon Agenda")

    data = {
        "Time": [
            "8:00 - 9:00 AM", "9:00 AM - 1:00 PM", "1:00 - 2:00 PM", "2:00 - 3:30 PM", "3:30 - 4:00 PM", "4:00 PM - Evening",
            "Early Morning - 1:00 PM", "1:00 - 2:00 PM", "2:00 - 4:00 PM", "4:00 - 8:00 PM"
        ],
        "Activity": [
            "Breakfast and Opening Remarks", "Tutorial Sessions (Led by experts)", "Lunch", "Keynote Speech and Problem Explanation",
            "Preliminary Team Findings", "Hackathon Kickoff",
            "Hackathon Continues", "Lunch", "Hackathon Concludes", "Team Presentations, Awards, and Reception Dinner"
        ],
        "Location": [
            "First Floor, TMC3 Retail Space", "First Floor, TMC3 Retail Space", "First Floor, TMC3 Retail Space", "First Floor, TMC3 Retail Space",
            "First Floor, TMC3 Retail Space", "Second Floor Workspace or First Floor, TMC3 Retail Space",
            "Second Floor Workspace", "TMC3 Atrium", "Second Floor Workspace", "TMC3 Atrium"
        ]
    }

    df = pd.DataFrame(data)

    st.table(df)

if __name__ == "__main__":
    main()
