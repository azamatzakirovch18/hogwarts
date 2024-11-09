from pygments.lexers import q
def winter_school_2022():
    import streamlit as st
    from data_engine import data
    import altair as alt

    with st.sidebar:
        st.markdown(
            """
            Winter school 2022 was amazing. There are 472 students applied with Google Forms but we took only 40 students. We did a lot of stuff with the students.

            ### Accurate Information

            - We covered a total of 472 candidates within 4 days.
            - All candidates came from 13 different regions.
            - Main candidates were from 9th grade to 11th grade and school students.

            ### Want to learn more?
            - Check out our [website](https://camp.newuu.uz)
            - Join Our [Telegram Channel](https://t.me/Hogwarts_NewUU)
            - Join Our [Instagram account](https://www.instagram.com/hogwarts_newuu)
            - Join Our [YouTube Channel](https://www.youtube.com/@campofnewuzbekistanuniversity)
            """
        )
        st.write("_____________________________")
        st.write("© New Uzbekistan University - 2022")

    st.write("# Winter School 2022")
    tab1, tab2, tab3 = st.tabs(
        ["Information about each region", "Compare 2 regions", "Compare 2 grades"])

    with tab1:
        left, right, very_right = st.columns(3)

        with left:
            regions = st.selectbox(
                "Please choose a region",
                options=[
                    "Andijan region",
                    "Bukhara region",
                    "Fergana region",
                    "Jizzakh Region",
                    "Karakalpakstan republic",
                    "Namangan Region",
                    "Navoiy region",
                    "Qashqadaryo Region",
                    "Samarkand region",
                    "Sirdaryo Region",
                    "Surxondaryo Region",
                    "Tashkent city",
                    "Tashkent region",
                    "Xorazm Region",
                ],
            )

        with right:
            grades = st.selectbox(
                "Please choose grade",
                options=["Grade 9", "Grade 10", "Grade 11"],
            )

        with very_right:
            days = st.multiselect(
                "Please choose a day",
                options=[
                    "December 23",
                    "December 24",
                    "December 25",
                    "December 26",
                    "December 27",
                ],
                default=["December 23", "December 24"],
            )

        df = data()
        converter = {
            "December 23": 23,
            "December 24": 24,
            "December 25": 25,
            "December 26": 26,
            "December 27": 27,
        }
        selected_days = [converter[day] for day in days]

        new_df = df[
            (df["REGION"] == regions)
            & (df["GRADE"] == grades)
            & df["DATE"].isin(selected_days)
            ]

        new_df = new_df.groupby(["DATE"]).count()
        new_df["COUNT"] = new_df["REGION"]
        new_df = new_df.drop(["REGION", "GRADE"], axis=1)

        import plotly.express as px

        fig = px.bar(
            new_df,
            x=new_df.index,
            y="COUNT",
            title=f'Number of applied candidates in "Winter School 2022" from {regions} {grades}th school boys',
            labels={"x": "Date", "COUNT": "Count"},
            color_discrete_sequence=["#636EFA"],
        )

        fig.update_layout(
            title_font_size=20,
            xaxis_title="Days in December",
            yaxis_title="Count",
            template="plotly_dark",
            xaxis=dict(tickmode="linear", tick0=25, dtick=1),
            yaxis=dict(tickformat="d")
        )

        st.plotly_chart(fig)

    with tab2:
        compare_left, compare_middle, compare_right = st.columns(3)
        with compare_left:
            first_region = st.selectbox(
                "Please choose a 1st region",
                options=[
                    "Andijan region",
                    "Bukhara region",
                    "Fergana region",
                    "Jizzakh Region",
                    "Karakalpakstan republic",
                    "Namangan Region",
                    "Navoiy region",
                    "Qashqadaryo Region",
                    "Samarkand region",
                    "Sirdaryo Region",
                    "Surxondaryo Region",
                    "Tashkent city",
                    "Tashkent region",
                    "Xorazm Region",
                ]
            )
        with compare_middle:
            second_region = st.selectbox(
                "Please choose a 2nd region",
                options=[
                    "Andijan region",
                    "Bukhara region",
                    "Fergana region",
                    "Jizzakh Region",
                    "Karakalpakstan republic",
                    "Namangan Region",
                    "Navoiy region",
                    "Qashqadaryo Region",
                    "Samarkand region",
                    "Sirdaryo Region",
                    "Surxondaryo Region",
                    "Tashkent city",
                    "Tashkent region",
                    "Xorazm Region",
                ]
            )

        with compare_right:
            compare_grades = st.selectbox(
                "Please choose grade for compare",
                options=["Grade 9", "Grade 10", "Grade 11"],
            )
        df_for_compare = df[
            (df["REGION"].isin([first_region, second_region]))
            & (df["GRADE"] == compare_grades)
            ]
        df_for_compare = df_for_compare.groupby(["REGION","DATE"]).count()
        df_for_compare["COUNT"] = df_for_compare["GRADE"]
        df_for_compare = df_for_compare.drop("GRADE", axis=1)

        import plotly.express as px
        import streamlit as st


        fig = px.line(
            df_for_compare.reset_index(),
            x="DATE",
            y="COUNT",
            color="REGION",
            title="Comparison of Applied Candidates Between Two Regions",
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

    with tab3:
        grade_left, grade_right = st.columns(2)

        with grade_left:
            grades_1 = st.selectbox(
                "Please choose 1st grade for compare",
                options=["Grade 9", "Grade 10", "Grade 11"],
            )

        with grade_right:
            grades_2 = st.selectbox(
                "Please choose 2nd grade for compare",
                options=["Grade 9", "Grade 10", "Grade 11"],
            )

        grades_df = df[
            (df["GRADE"].isin([grades_1, grades_2]))
        ]

        grades_df = grades_df.groupby(["GRADE", "DATE"]).count()

        grades_df["COUNT"] = grades_df["REGION"]

        grades_df = grades_df.drop( "REGION", axis=1)

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