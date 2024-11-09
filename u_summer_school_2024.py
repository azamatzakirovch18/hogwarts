def summer_school_2024():
    import streamlit as st
    from data_engine import data_summer_2024

    with st.sidebar:
        st.markdown(
            """
            Summer school 2024 was amazing. This time we made some changes. We are covered 905 school and university students.

            ### Accurate Information

            - We are covered total 905 candidates with in 12 days
            - All candidates come from 14 different regions 
            - Main candidates were from 9th grade to 11th grate and school students and from 1st to 4th grade university students

            ### Want to learn more?
            - Check out our [website](https://camp.newuu.uz)
            - Join Our  [   Telegram Channel](https://t.me/Hogwarts_NewUU)
            - Join Our [    Instagram account](https://www.instagram.com/hogwarts_newuu)
            - Join Our [    Youtube Channel](https://www.youtube.com/@campofnewuzbekistanuniversity)
        """
        )
        st.write("_____________________________")
        st.write("© New Uzbekistan University - 2024")
    st.write("# Summer School 2024")
    tab1, tab2, tab3 = st.tabs(
        ["Information about each region", "Compare 2 regions", "Compare 2 grades"])

    with tab1:
        left, right, very_right = st.columns(3)
        with left:
            regions = st.selectbox(
                "Please choose a region",
                options=['Andijan',
                         'Bukhara',
                         'Fergana',
                         'Jizzakh',
                         'Karakalpakistan',
                         'Kashkadarya',
                         'Khorazm',
                         'Namangan',
                         'Navoi',
                         'Samarkand',
                         'Sirdarya',
                         'Surkhandarya',
                         'Tashkent city',
                         'Tashkent region'
                         ],
            )
        with right:
            grades = st.selectbox(
                "Please choose grade",
                options=['9.0', '11.0', '10.0', 'Freshman', 'Sophomore', 'Junior', 'Senior'],
            )
        with very_right:
            days = st.multiselect(
                "Please choose a day",
                options=[
                    "May 16",
                    "May 24",
                    "May 25",
                    "May 26",
                    "May 27",
                    "May 28",
                    "May 29",
                    "May 30",
                    "May 31",
                    "June 1",
                    "June 2",
                    "June 3"
                ],
                default=["May 16", "May 24"],
            )
        df = data_summer_2024()
        convert = {
            "May 16": 16,
            "May 24": 24,
            "May 25": 25,
            "May 26": 26,
            "May 27": 27,
            "May 28": 28,
            "May 29": 29,
            "May 30": 30,
            "May 31": 31,
            "June 1": 1,
            "June 2": 2,
            "June 3": 3
        }
        selected_day = [convert[day] for day in days]
        new = df[
            (df["REGION"] == regions)
            & (df["GRADE"] == grades)
            & df["DATE"].isin(selected_day)
        ]
        new = new.groupby(["DATE"]).count()
        new["COUNT"] = new["REGION"]
        new = new.drop(["REGION", "GRADE"], axis=1)

        import plotly.express as px

        fig = px.bar(
            new,
            x=new.index,
            y="COUNT",
            title=f'Number of applied candidates in "Summer School 2024" from {regions}',
            labels={"x": "Date", "COUNT": "Count"},
            color_discrete_sequence=["#636EFA"],
        )

        # You can adjust layout features
        fig.update_layout(
            title_font_size=20,
            xaxis_title="Days in May & July",
            yaxis_title="Count",
            template="plotly_dark",
        )
        st.plotly_chart(fig)


    with tab2:
        compare_left, compare_middle, compare_right = st.columns(3)
        with compare_left:
            first_region = st.selectbox(
                "Please choose a 1st region",
                options=['Andijan', 'Bukhara', 'Fergana', 'Jizzakh', 'Karakalpakistan',  'Kashkadarya', 'Khorazm', 'Namangan', 'Navoi', 'Samarkand',  'Sirdarya', 'Surkhandarya', 'Tashkent city', 'Tashkent region']

            )
        with compare_middle:
            second_region = st.selectbox(
                "Please choose a 2nd region",
                options=['Andijan', 'Bukhara', 'Fergana', 'Jizzakh', 'Karakalpakistan', 'Kashkadarya', 'Khorazm',
                         'Namangan', 'Navoi', 'Samarkand', 'Sirdarya', 'Surkhandarya', 'Tashkent city',
                         'Tashkent region']

            )

        with compare_right:
            compare_grades = st.selectbox(
                "Please choose grade for compare",
                options=[9, 10, 11, "Freshmen", "Sophomore", "Junior", "Senior"],
            )
        df_for_compare = df[
            (df["REGION"].isin([first_region, second_region]))
            & (df["GRADE"] == compare_grades)
            ]
        df_for_compare = df_for_compare.groupby(["REGION","DATE"]).count()
        df_for_compare["COUNT"] = df_for_compare["GRADE"]
        df_for_compare = df_for_compare.drop(["GRADE"], axis=1)

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
        st.write(df_for_compare)

    with tab3:
        grade_left, grade_right = st.columns(2)

        with grade_left:
            grades_1 = st.selectbox(
                "Please choose 1st grade for compare",
                options=[9, 10, 11, "Freshmen", "Sophomore", "Junior", "Senior"],
            )

        with grade_right:
            grades_2 = st.selectbox(
                "Please choose 2nd grade for compare",
                options=[9, 10, 11, "Freshmen", "Sophomore", "Junior", "Senior"],
            )

        grades_df = df[
            (df["GRADE"].isin([grades_1, grades_2]))
        ]

        grades_df = grades_df.groupby(["GRADE", "DATE"]).count()

        grades_df["COUNT"] = grades_df["REGION"]

        grades_df = grades_df.drop(["REGION"], axis=1)

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