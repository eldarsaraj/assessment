# Data import and cleaning
import pandas as pd
import numpy as np

csv_path = 'Pre-survey-final.csv'

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df.dropna(inplace=True)
    rename_dict = {'Are you:': 'Level',
                   'What is your major?': 'Major',
                    'What is the highest level of education your parents/guardians have completed? ': 'Parental education',
                    'How many books do you or your family have at home?' : 'Amount of books at home',
                    'How comfortable are you in reading, understanding, and communicating in English?': 'English proficiency',
                    'Do you work?' : 'Working students',
                    'Do you live:' : 'Living with',
                    'What was your GPA in high-school? ' : 'GPA'
                  }
    df.rename(columns=rename_dict, inplace=True)
    return df

import pandas as pd

def categorize_majors(data):
    unique_majors = data['Major'].unique()

    mapping = {
        'Liberal Arts': ['Liberal Arts', 'Ethnic and Race Studies'],
        'Sciences': ['science of forensics', 'Science for Health', 'Forensic Science',
                     'health science', 'Health Science', 'Engineering Science',
                     'Sciences in Health', 'Science for health', 'Applied Science',
                     'Science for Health professions (Vet Technician)', 'engineering science', 'Engineering science'],
        'Humanities': ['Jazz and Popular Music', 'digital marketing',
                       'Not Sure but Undecided', 'Critical Thinking & Justice',
                       'digital marketing', 'Communication Studies', 'Sociology',
                       'Human Services', 'Psychologist', '9-14 program',
                       'My school primarily focuses on production.'],
        'Others': ['Business Administration and Management', 'graduated already',
                   'Nusing', 'Multimedia programming and design',
                   'Public Health', 'Forensics', 'CRT-100 Senior Year',
                   'I don’t have a major', 'Criminal Justice', 'Education']
    }

    # Create a DataFrame with the unique majors
    df = pd.DataFrame({'Major': unique_majors})

    # Create a new 'Category' column based on the mapping dictionary
    df['Major group'] = df['Major'].apply(lambda x: next((k for k, v in mapping.items() if x in v), 'Others'))
    data['Major group'] = df['Major group']
    data['Major group'] = data['Major group'].fillna('None')
    return data

def categorize_age(data):
    # Remove non-numeric entries from 'Age' column
    data = data[pd.to_numeric(data['Age'], errors='coerce').notnull()]
    data['Age'] = data['Age'].astype(int)

    # Create a new column 'AgeGroup' and populate it based on 'Age'
    bins = [0, 18, 25, 30, 40]
    labels = ['0-18', '19-25', '26-30', '31-40']
    data['Age group'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)
    data['Age group'] = data['Age group'].astype(str)

    return data

gray_colors = ['#333333', '#4D4D4D', '#666666', '#7F7F7F', '#999999', '#B3B3B3', '#CCCCCC']

def clean_english_proficiency_column(df):
    df['English proficiency'] = df['English proficiency'].str.replace('.', '', regex=False)
    df['English proficiency'] = df['English proficiency'].str.replace('Comfortable enough to understand most things', 'Comfortable enough', regex=False)
    return df

def clean_education_column(data):
    data['Parental education'] = data['Parental education'].str.replace('.', '', regex=False)
    data['Parental education'] = data['Parental education'].replace('Did not complete high school', 'No high school')
    
    return data

def clean_working_students_column(data):
    data['Working students'] = data['Working students'].str.replace('.', '', regex=False)
    data['Working students'] = data['Working students'].str.replace('Yes, full time', 'Full time', regex=False)
    data['Working students'] = data['Working students'].str.replace('Yes, part-time', 'Part time', regex=False)
    return data

def clean_living(data):
    data['Living with'] =  data['Living with'].str.replace('With parents', 'Parents', regex=False)
    data['Living with'] =  data['Living with'].str.replace('By yourself', 'Myself', regex=False)
    return data

def clean_gpa_column(df):
    df['GPA'] = pd.to_numeric(df['GPA'], errors='coerce')
    df['GPA'] = df['GPA'].astype(str)
    return df