import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.set_page_config(
    layout="wide",            
    page_title="CRT Assessment",      
    page_icon="CRT.ico"   
)

st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
""", unsafe_allow_html=True)


def local_css(file_name):
    with open(file_name, 'r') as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css('style.css')

image_path = 'images/assessment.png'
st.image(image_path, width=200, use_column_width=False) 

st.markdown('''
<div class="text-box">
    <i class="fas fa-question-circle"></i> Analytical report / Critical Thinking (CRT) / Fall 2023.
</div>
''', unsafe_allow_html=True)   

# Sidebar Table of Contents
st.sidebar.title('Contents')

# Load data
from data_utils import load_data
data = load_data('Pre-survey-final.csv')

# Define pages
pages = {
    'Demographics': 'demo',
    'Scores': 'scores',
    'Datasets': 'datasets'
}

if 'page' not in st.session_state:
    st.session_state.page = 'demo'  # default page

for page_name, page_code in pages.items():
    if st.sidebar.button(page_name):
        st.session_state.page = page_code

if st.session_state.page == 'demo':
    st.text('')
    st.image('images/demographics.png', width=150, use_column_width=False)    
          
    col1, col2, col3, col4 = st.columns(4)
    
    
    with col1:
        st.write('')
        chart = alt.Chart(data).mark_bar().encode(
                x=alt.X('Level', axis=None),
                y=alt.Y('count()', axis=alt.Axis(title='Count')),
                color=alt.Color('Level', scale=alt.Scale(
                    domain=['Freshman', 'Sophomore'],
                    range=['#B22222', 'gray'])
                )
            ).properties(
                width=alt.Step(30)  
            )
        
        st.altair_chart(chart)
       
    st.divider()
    
    with col2:
        st.write('')
        chart = alt.Chart(data).mark_bar().encode(
                x=alt.X('Gender', axis=None),
                y=alt.Y('count()', axis=alt.Axis(title='Count')),
                color=alt.Color('Gender', scale=alt.Scale(
                    domain=['Male', 'Female'],
                    range=['gray', '#B22222'])
                )
            ).properties(
                width=alt.Step(30)  
            )
         
        st.altair_chart(chart)    
  
    with col3:
        st.write('')
        from data_utils import categorize_majors
        categorized_data = categorize_majors(data)

        chart = alt.Chart(categorized_data).mark_bar().encode(
                x=alt.X('Major group', axis=None),  # Specify the type as 'N' for Nominal
                y=alt.Y('count()', axis=alt.Axis(title='Count')),
                color=alt.Color('Major group', scale=alt.Scale(  
                    domain=['Liberal Arts', 'Sciences', 'Others', 'Humanities', 'None'],
                    range=['#333333', '#4D4D4D', '#666666', '#7F7F7F', '#B22222'])
                )
            ).properties(
                width=alt.Step(30)
            )

        st.altair_chart(chart) 
        
    with col4:
        from data_utils import categorize_age
        categorized_age = pd.DataFrame(categorize_age(data))
        
        chart = alt.Chart(categorized_age).mark_bar().encode(
                x=alt.X('Age group', axis=None),  
                y=alt.Y('count()', axis=alt.Axis(title='Count')),
                color=alt.Color('Age group', scale=alt.Scale(
                    domain=['0-18', '19-25', '26-30', '31-40'],
                    range=['#4D4D4D', '#B22222', '#666666', '#7F7F7F'])
                )
            ).properties(
                width=alt.Step(30)
            )
 
        st.altair_chart(chart) 

    st.write('')
    #st.markdown('''<div class="text-box"></div>''', unsafe_allow_html=True) 
    st.write('')
    
    col5, col6, col7 = st.columns(3)
    
    st.divider()
    
    with col5:
        from data_utils import clean_education_column
        clean_ed = clean_education_column(data)
        chart = alt.Chart(clean_ed).mark_bar().encode(
                x=alt.X('Parental education:N', axis=None),
                y=alt.Y('count()', axis=alt.Axis(title='Count')),
                color=alt.Color('Parental education:N', scale=alt.Scale(
                domain=['Graduate degree', 'High-school degree',
                'No high school', 'College degree'],
                range=['#4D4D4D', '#B22222', '#666666', '#7F7F7F']))
                ).properties(
                    width=alt.Step(30)  
                ).properties(
                    
                )
        
        st.altair_chart(chart)

    with col6:
        chart = alt.Chart(clean_ed).mark_bar().encode(
                x=alt.X('Amount of books at home:N', axis=None),
                y=alt.Y('count()', axis=alt.Axis(title='Count')),
                color=alt.Color('Amount of books at home:N', scale=alt.Scale(
                domain=['More than 50', 'Between 5 and 20', 'Less than 5',
                'Between 20 and 50'],
                range=['#4D4D4D', '#B22222', '#666666']))
                ).properties(
                    width=alt.Step(30)  
                ).properties(
                    
                )
        
        st.altair_chart(chart)
    
    with col7:
        from data_utils import clean_english_proficiency_column
        clean_eng = clean_english_proficiency_column(data)
        chart = alt.Chart(clean_ed).mark_bar().encode(
                x=alt.X('English proficiency:N', axis=None),
                y=alt.Y('count()', axis=alt.Axis(title='Count')),
                color=alt.Color('English proficiency:N', scale=alt.Scale(
                domain=['Absolutely comfortable', 'Somewhat comfortable',
                'Fairly comfortable', 'Comfortable enough',
                'Not comfortable at all'], 
                range=['#B22222', '#333333', '#4D4D4D', '#666666', '#7F7F7F']))
                ).properties(
                    width=alt.Step(30)  
                ).properties(
                    
                )
        
        st.altair_chart(chart)
    
    st.write('')
    #st.markdown('''<div class="text-box"></div>''', unsafe_allow_html=True) 
    st.write('')
    
    col8, col9, col10 = st.columns(3)
        
    with col8:
        from data_utils import clean_working_students_column
        working = clean_working_students_column(data)
        
        chart = alt.Chart(working).transform_aggregate(
                total='count()',
                groupby=['Working students']).transform_window(
                sort=[{'field': 'total'}],
                cum_total='sum(total)').mark_arc(innerRadius=0.1).encode(
                theta=alt.Theta('total:Q', stack=True),
                color=alt.Color('Working students:N',
                scale=alt.Scale(domain=['Full time', 'Part time', 'No'],
                range=['#B22222', '#D9534F', 'gray'])),
                tooltip=['Working students', 'total:Q']).properties(
                width=400,
                height=400)

        st.altair_chart(chart)
        
    with col9:
        from data_utils import clean_living
        living = clean_living(data)
        
        chart = alt.Chart(living).transform_aggregate(
                total='count()',
                groupby=['Living with']).transform_window(
                sort=[{'field': 'total'}],
                cum_total='sum(total)').mark_arc(innerRadius=0.1).encode(
                theta=alt.Theta('total:Q', stack=True),
                color=alt.Color('Living with:N',
                scale=alt.Scale(domain=['Parents', 'Myself'],
                range=['#D9534F', 'gray'])),
                tooltip=['Living with', 'total:Q']).properties(
                width=350,
                height=400)

        st.altair_chart(chart)
    
    with col10:
        from data_utils import clean_gpa_column
        gpa = clean_gpa_column(data)      
        chart = alt.Chart(gpa).mark_bar().encode(
                x=alt.X('GPA:N', axis=None),  
                y=alt.Y('count()', axis=alt.Axis(title='Count')),
                color=alt.Color('GPA:N', scale=alt.Scale(  
                    domain=['3.0', '3.3', '4.0', '3.7', '2.7', '2.3', '1.3', '2.0', '1.7'],
                    range=['#B22222', '#1c1c1c', '#383838', '#555555', '#717171', '#8d8d8d', '#aaaaaa', '#c6c6c6', '#e2e2e2'])
                )
            ).properties(
                width=alt.Step(30)
            )

        st.altair_chart(chart)
 
# SCORES    
    
elif st.session_state.page == 'scores':
    st.write('')
    st.image('images/scores.png', width=150, use_column_width=False)  
  
    from stats_utils import calculate_student_scores, calculate_post_scores, bootstrap_scores
    from data_utils import categorize_majors, categorize_age, load_data
   
    post_survey = load_data('post-survey.csv')
    post_survey = calculate_post_scores(post_survey)
    scores = calculate_student_scores(data)
    
    scores['Post-survey'] = post_survey['Post-survey']
    
    melted_scores = pd.melt(scores, 
                         id_vars=[], 
                         value_vars=['Pre-survey', 'Post-survey'],
                         var_name='Score Type', 
                         value_name='Score')
    
    pre_mean_value = np.mean(scores['Pre-survey'])
    pre_std_value = np.std(scores['Pre-survey'])
    post_mean_value = np.mean(scores['Post-survey'])
    post_std_value = np.std(scores['Post-survey'])

    
    st.write('')
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label='Pre-survey mean score', value=round(pre_mean_value, 1)) 
    with col2:
        st.metric(label='Post-survey mean score', value=round(post_mean_value, 1), delta=(round(post_mean_value - pre_mean_value, 1))) 
    with col3:
        st.metric(label='Pre-survey standard deviation', value=round(pre_std_value, 1)) 
    with col4:
        st.metric(label='Post-survey standard deviation', value=round(post_std_value, 1), delta=(round(post_std_value - pre_std_value, 1)))
    
    st.divider()
    st.write('')

    col4, col5 = st.columns(2)
    
    with col4:
        
        bin_size = 1  
        min_bin = int(melted_scores['Score'].min())
        max_bin = int(melted_scores['Score'].max())

        melted_scores['Bin'] = pd.cut(melted_scores['Score'], bins=range(min_bin, max_bin + bin_size, bin_size))

        # Calculate mid-point of bin
        melted_scores['Mid'] = melted_scores['Bin'].apply(lambda x: x.left + (x.right - x.left) / 2)

        # Add offset to mid-point based on 'Score Type'
        melted_scores['Mid_with_offset'] = melted_scores.apply(
            lambda row: row['Mid'] + (0.2 if row['Score Type'] == 'Pre-survey' else -0.2),
            axis=1
        )

        chart = alt.Chart(melted_scores).mark_bar(size=20).encode(
            x=alt.X('Mid_with_offset:Q', title='Scores'),
            y=alt.Y('count()', title='Count'),
            color=alt.Color('Score Type:N', scale=alt.Scale(domain=['Pre-survey', 'Post-survey'], range=['#4D4D4D', '#B22222']))
        ).properties(width=600, height=350)

        st.altair_chart(chart)
        
    with col5:
        filtered_melted_scores = melted_scores.dropna(subset=['Score'])

        area_plot = alt.Chart(melted_scores).transform_density(
                    density='Score',
                    bandwidth=0.3,  
                    groupby=['Score Type'],
                    as_=['Score', 'Density']
                ).mark_area().encode(
                    x='Score:Q',
                    y='Density:Q',
                    color=alt.Color('Score Type:N', scale=alt.Scale(domain=['Pre-survey', 'Post-survey'], range=['#4D4D4D', '#B22222']))
                ).properties(
                    width=600,
                    height=350
                )

        st.altair_chart(area_plot)

    st.divider()
    st.write('')

    col6, col7 = st.columns([0.7, 0.3])  

    scores = categorize_majors(scores)
    scores = categorize_age(scores)
    
    # Radio button section in the right column
    variables = ['Level', 'Major group', 'Gender', 'Age group', 'Parental education', 'English proficiency', 'Working students', 
                 'Living with', 'GPA']
    selected_var = col7.radio('', variables, index=3)  # Default to "Age"
    
    scores['ScoreFrequency'] = scores.groupby(variables)['Pre-survey'].transform('count')
    
    # Create scatter plots based on the selected variable
    if scores[selected_var].dtype == 'object':  # Categorical variables
        chart = alt.Chart(scores).mark_circle(color='#B22222', opacity=1).encode(
            x=alt.X('Pre-survey:Q', axis=alt.Axis(title='Scores')), # "Q" for quantitative data type
            y=alt.Y(f"{selected_var}:O", axis=alt.Axis(title=None)),
            size=alt.Size('ScoreFrequency:Q', legend=None),
            tooltip=['Pre-survey:Q', f"{selected_var}:O"]
        ).properties(width=800, height=400)
        
    else:  # Numerical variables
        chart = alt.Chart(scores).mark_circle(color='#B22222', opacity=1).encode(
            x=alt.X('Pre-survey:Q', axis=alt.Axis(title='Scores')),
            y=alt.Y(f"{selected_var}:Q", axis=alt.Axis(title=None)),
            size=alt.Size('ScoreFrequency:Q', legend=None),
            tooltip=['Pre-survey:Q', f"{selected_var}:Q"]
        ).properties(width=800, height=400)

    # Render the chart in the left column
    col6.altair_chart(chart)
    
    st.divider()
    col8, col9, col10 = st.columns(3)
    
    with col8:
        post_survey = calculate_post_scores(load_data('post-survey.csv'))
        pre_survey = calculate_student_scores(load_data('Pre-survey-final.csv'))
        
        pre_avg = pre_survey.groupby('Gender')['Pre-survey'].mean()
        post_avg = post_survey.groupby('Gender')['Post-survey'].mean()
        
        pre_avg = pre_avg.reset_index().rename(columns={'Pre-survey': 'Average score', 'Gender': 'Gender'})
        pre_avg['Survey'] = 'Pre'

        post_avg = post_avg.reset_index().rename(columns={'Post-survey': 'Average score', 'Gender': 'Gender'})
        post_avg['Survey'] = 'Post'

        combined = pd.concat([pre_avg, post_avg])
        
        chart = alt.Chart(combined).mark_bar().encode(
                x=alt.X('Survey:N', title=None, sort=['Pre', 'Post']),
                y=alt.Y('Average score:Q', title='Average Score'),
                color=alt.Color('Survey:N', scale=alt.Scale(domain=['Pre', 'Post'], range=['gray', '#B22222'])),
                column='Gender:N'
            )
        
        st.altair_chart(chart)
        
    with col9:
        lev_pre = pre_survey.groupby('Level')['Pre-survey'].mean()
        lev_post = post_survey.groupby('Level')['Post-survey'].mean()
        
        lev_pre = lev_pre.reset_index().rename(columns={'Pre-survey': 'Average score', 'Level': 'Level'})
        lev_pre['Survey'] = 'Pre'

        lev_post = lev_post.reset_index().rename(columns={'Post-survey': 'Average score', 'Level': 'Level'})
        lev_post['Survey'] = 'Post'
        
        lev_combined = pd.concat([lev_pre, lev_post])

        chart = alt.Chart(lev_combined).mark_bar().encode(
                x=alt.X('Survey:N', title=None, sort=['Pre', 'Post']),
                y=alt.Y('Average score:Q', title='Average Score'),
                color=alt.Color('Survey:N', scale=alt.Scale(domain=['Pre', 'Post'], range=['gray', '#B22222'])),
                column='Level:N'
            )
        
        st.altair_chart(chart)
        
    with col10:
        liv_pre = pre_survey.groupby('Living with')['Pre-survey'].mean()
        liv_post = post_survey.groupby('Living with')['Post-survey'].mean()
        
        liv_pre = liv_pre.reset_index().rename(columns={'Pre-survey': 'Average score', 'Living with': 'Living with'})
        liv_pre['Survey'] = 'Pre'
        liv_pre['Living with'] = liv_pre['Living with'].replace({'By yourself': 'Yourself', 'With parents': 'Parents'})

        liv_post = liv_post.reset_index().rename(columns={'Post-survey': 'Average score', 'Living with': 'Living with'})
        liv_post['Survey'] = 'Post'
        liv_post['Living with'] = liv_post['Living with'].replace({'By yourself': 'Yourself', 'With parents': 'Parents'})

        
        liv_combined = pd.concat([liv_pre, liv_post])

        chart = alt.Chart(liv_combined).mark_bar().encode(
                x=alt.X('Survey:N', title=None, sort=['Pre', 'Post']),
                y=alt.Y('Average score:Q', title='Average Score'),
                color=alt.Color('Survey:N', scale=alt.Scale(domain=['Pre', 'Post'], range=['gray', '#B22222'])),
                column='Living with:N'
            )
        
        st.altair_chart(chart)
       



        


    
elif st.session_state.page == 'datasets':
    st.header('Datasets')
    # Content for conclusion
    
    from stats_utils import calculate_student_scores, calculate_post_scores
    from data_utils import load_data
    
    st.write('Pre-survey')
    pre_survey = load_data('Pre-survey-final.csv')
    #pre_survey = pre_survey.rename(columns={'Pre-survey': 'Survey score'})
    pre_survey

    
    st.divider()
    
    st.write('Post-survey')
    post_survey = load_data('post-survey.csv')
    #post_survey = calculate_post_scores(post_survey)
    #post_survey = post_survey.rename(columns={'Post-survey': 'Survey score'})
    post_survey

   



 