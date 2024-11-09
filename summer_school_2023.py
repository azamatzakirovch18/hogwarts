def summer_school_2023():
    import streamlit as st
    from data_engine import data_summer_2023

    with st.sidebar:
        st.markdown(
            """
            Summer school 2023 was amazing. There are 1521  students applied with google forms but we took only 40 students. We did a lot of stuffs with students
    
            ### Accurate Information
    
            - We are covered total 1521 candidates with in 9 days
            - All candidates come from 13 different regions 
            - Main candidates were from 9th grade to 11th grate and school students
    
            ### Want to learn more?
            - Check out our [website](https://camp.newuu.uz)
            - Join Our  [   Telegram Channel](https://t.me/Hogwarts_NewUU)
            - Join Our [    Instagram account](https://www.instagram.com/hogwarts_newuu)
            - Join Our [    Youtube Channel](https://www.youtube.com/@campofnewuzbekistanuniversity)
        """
        )
        st.write("_____________________________")
        st.write("© New Uzbekistan University - 2023")

    st.write("# Summer School 2023")
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
                    "Jizzakh region",
                    "Kashkadarya region",
                    "Khorezm region",
                    "Namangan region",
                    "Navoiy region",
                    "Republic of Karakalpakstan",
                    "Samarkand region",
                    "Sirdarya region",
                    "Surkhandarya region",
                    "Tashkent region",
                ],
            )

        with right:
            grades = st.selectbox(
                "Please choose grade",
                options=["9th", "10th", "11th"],
            )
        with very_right:
            days = st.multiselect(
                "Please choose a day",
                options=[
                    "July 17",
                    "July 18",
                    "July 19",
                    "July 20",
                    "July 21",
                    "July 22",
                    "July 23",
                    "July 24",
                    "July 25",
                ],
                default=["July 17", "July 18"],
            )
        df = data_summer_2023()
        convert = {
            "July 17": 17,
            "July 18": 18,
            "July 19": 19,
            "July 20": 20,
            "July 21": 21,
            "July 22": 22,
            "July 23": 23,
            "July 24": 24,
            "July 25": 25,
        }
        selected_day = [convert[day] for day in days]

        # Filter the dataframe
        new = df[
            (df["REGION"] == regions)
            & (df["GRADE"] == grades)
            & df["DATE"].isin(selected_day)
        ]

        new = new.groupby(["DATE"]).count()
        new["COUNT"] = new["REGION"]
        new = new.drop(["REGION", "GRADE"], axis=1)

        # st.write(new)

        import plotly.express as px

        fig = px.bar(
            new,
            x=new.index,
            y="COUNT",
            title=f'Number of applied candidates in "Summer School 2023" from {regions} {grades}th school boys',
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
        compare_left, compare_middle, compare_right = st.columns(3)
        with compare_left:
            first_region = st.selectbox(
                "Please choose a 1st region",
                options=['Andijan region',
                         'Bukhara region',
                         'Fergana region',
                         'Jizzakh region',
                         'Kashkadarya region',
                         'Khorezm region',
                         'Namangan region',
                         'Navoiy region',
                         'Republic of Karakalpakstan',
                         'Samarkand region',
                         'Sirdarya region',
                         'Surkhandarya region',
                         'Tashkent region']
            )
        with compare_middle:
            second_region = st.selectbox(
                "Please choose a 2nd region",
                options=['Andijan region',
                         'Bukhara region',
                         'Fergana region',
                         'Jizzakh region',
                         'Kashkadarya region',
                         'Khorezm region',
                         'Namangan region',
                         'Navoiy region',
                         'Republic of Karakalpakstan',
                         'Samarkand region',
                         'Sirdarya region',
                         'Surkhandarya region',
                         'Tashkent region']
            )

        with compare_right:
            compare_grades = st.selectbox(
                "Please choose grade for compare",
                options=['11th', '9th', '10th'],
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

    with tab3:
        grade_left, grade_right = st.columns(2)

        with grade_left:
            grades_1 = st.selectbox(
                "Please choose 1st grade for compare",
                options=['11th', '9th', '10th']
            )

        with grade_right:
            grades_2 = st.selectbox(
                "Please choose 2nd grade for compare",
                options=['11th', '9th', '10th']
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