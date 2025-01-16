import streamlit as st

def main():
    st.title("Hackathon Agenda")

    st.header("Day 1 – Friday, April 4")

    st.subheader("8:00 - 9:00 AM")
    st.write("Breakfast and Opening Remarks")
    st.write("Location: First Floor, TMC3 Retail Space")

    st.subheader("9:00 AM - 1:00 PM")
    st.write("Tutorial Sessions (Led by experts)")
    st.write("Location: First Floor, TMC3 Retail Space")
    st.caption("Attendees (~50) can follow on laptops. Ensure your devices are charged or bring portable power sources.")

    st.subheader("1:00 - 2:00 PM")
    st.write("Lunch")
    st.write("Location: First Floor, TMC3 Retail Space")

    st.subheader("2:00 - 3:30 PM")
    st.write("Keynote Speech and Problem Explanation")
    st.write("Location: First Floor, TMC3 Retail Space")

    st.subheader("3:30 - 4:00 PM")
    st.write("Preliminary Team Findings")
    st.write("Location: First Floor, TMC3 Retail Space")

    st.subheader("4:00 PM - Evening")
    st.write("Hackathon Kickoff")
    st.write("Location: Second Floor Workspace or First Floor, TMC3 Retail Space")
    st.write("Dinner Provided: Pizza and Coffee")

    st.header("Day 2 – Saturday, April 5")

    st.subheader("Early Morning - 1:00 PM")
    st.write("Hackathon Continues")
    st.write("Location: Second Floor Workspace")
    st.write("Breakfast Buffet with Additional Coffee")

    st.subheader("1:00 - 2:00 PM")
    st.write("Lunch")
    st.write("Location: TMC3 Atrium")

    st.subheader("2:00 - 4:00 PM")
    st.write("Hackathon Concludes")
    st.write("Location: Second Floor Workspace")

    st.subheader("4:00 - 8:00 PM")
    st.write("Team Presentations, Awards, and Reception Dinner")
    st.write("Location: TMC3 Atrium")

if __name__ == "__main__":
    main()
