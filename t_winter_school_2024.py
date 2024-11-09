def win_24():
    import streamlit as st
    from data_engine import data_winter_2024

    with st.sidebar:
        st.markdown(
            """
            Summer school 2023 was amazing. There are 1873  students applied with google forms but we took only 40 students. We did a lot of stuffs with students

            ### Accurate Information

            - We are covered total 1873 candidates with in 9 days
            - All candidates come from 13 different regions 
            - Main candidates were from 8th grade to 11th grate and school students

            ### Want to learn more?
            - Check out our [website](https://camp.newuu.uz)
            - Join Our  [   Telegram Channel](https://t.me/Hogwarts_NewUU)
            - Join Our [    Instagram account](https://www.instagram.com/hogwarts_newuu)
            - Join Our [    Youtube Channel](https://www.youtube.com/@campofnewuzbekistanuniversity)
        """
        )
        st.write("_____________________________")
        st.write("© New Uzbekistan University - 2023")

    st.write("# Winter School 2024")
    tab1, tab2 = st.tabs(
        ["Total","Compare 2 grades"])

    with tab1:
        right, very_right = st.columns(2)


        with right:
            grades = st.selectbox(
                "Please choose grade",
                options=[8,9,10,11],
            )
        with very_right:
            days = st.multiselect(
                "Please choose a day",
                options=[
                    "Feb 1",
                    "Feb 2",
                    "Feb 3",
                    "Feb 4",
                    "Feb 5",
                    "Feb 6",
                    "Feb 7",
                    "Feb 8",
                    "Feb 9",
                    "Feb 10",
                    "Feb 11",
                    "Feb 12",
                    "Jan 31",
                ],
                default=["Feb 1", "Feb 7"],
            )
        df = data_winter_2024()
        convert = {
            "Feb 1" : 1,
            "Feb 2" : 2,
            "Feb 3" : 3,
            "Feb 4" : 4,
            "Feb 5" : 5,
            "Feb 6" : 6,
            "Feb 7" : 7,
            "Feb 8" : 8,
            "Feb 9" : 9,
            "Feb 10" : 10,
            "Feb 11" : 11,
            "Feb 12" : 12,
            "Jan 31" : 31,
        }
        selected_day = [convert[day] for day in days]

        # Filter the dataframe
        new = df[
            (df["GRADE"] == grades)
            & df["DATE"].isin(selected_day)
            ]

        new = new.groupby(["DATE"]).count()
        new["COUNT"] = new["GRADE"]
        new = new.drop(["GRADE"], axis=1)

        # st.write(new)

        import plotly.express as px

        fig = px.bar(
            new,
            x=new.index,
            y="COUNT",
            title=f'Number of applied candidates in "Winter School 2024" in {grades}th school boys',
            labels={"x": "Date", "COUNT": "Count"},
            color_discrete_sequence=["#636EFA"],
        )

        # You can adjust layout features
        fig.update_layout(
            title_font_size=20,
            xaxis_title="Days in July",
            yaxis_title="Count",
            template="plotly_dark",
            xaxis=dict(tickmode="linear", tick0=25, dtick=1),
            yaxis=dict(tickformat="d")
        )

        st.plotly_chart(fig)


    with tab2:
        grade_left, grade_right = st.columns(2)

        with grade_left:
            grades_1 = st.selectbox(
                "Please choose 1st grade for compare",
                options=[11, 10, 9, 8]
            )

        with grade_right:
            grades_2 = st.selectbox(
                "Please choose 2nd grade for compare",
                options=[11, 10, 9, 8]
            )

        grades_df = df[
            (df["GRADE"].isin([grades_1, grades_2]))
        ]

        grades_df['oo'] = grades_df['GRADE']


        grades_df = grades_df.groupby(["GRADE", "DATE"]).count()

        grades_df["COUNT"] = grades_df["oo"]

        grades_df = grades_df.drop(["oo"], axis=1)

        import plotly.express as px

        fig = px.line(
            grades_df.reset_index(),
            x="DATE",
            y="COUNT",
            color="GRADE",
            title="Comparison of Applied Candidates Between Two Grades",
            labels={"DATE": "Days in December", "COUNT": "Number of Candidates"},
        )

        fig.update_layout(
            xaxis_title="Days in December",
            yaxis_title="Number of Candidates",
            title_font_size=20,
            template="plotly_dark",
            xaxis=dict(tickmode="linear", tick0=25, dtick=1),
            yaxis=dict(tickformat="d")
        )

        st.plotly_chart(fig)