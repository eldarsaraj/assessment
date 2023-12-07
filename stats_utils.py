import pandas as pd



def calculate_student_scores(df):
    # Complete dictionary of correct answers keyed by column name
    correct_answers_by_name = {
        'In the previous question, which statement is used as support for the main claim? ': 'School uniforms reduce distractions and bullying.',
        'A company has seen a 20% decrease in sales due to a new competitor. \nWhat could be a potential first step to address this problem?': "Analyze the competitor's strengths and weakneses",
        "Continue thinking about the scenario from the previous question. Let's say that you decided to analyze the competitor's strengths. \nThey have a more user-friendly website and faster delivery times. \nWhat could be your next step?" : "Improve the company's website usability and delivery times.",
        'Consider the claim: \n"Diet rich in fruits and vegetables leads to better health." \nWhich of the following would be strongest evidence for this claim?' : 'A scientific study showing lower rates of disease in people who eat more fruits and vegetables.',
        'Continue thinking about the scenario from the previous question.\n\nBased on your selected answer about the best evidence, how strongly does it support the claim (0-weak, 2-strong)?' : 2,
        'Consider the argument: \n"All birds can fly. Penguins are birds. Therefore, penguins can fly." \nWhat is wrong with this argument?': 'One of the sentences is not true.',
        'Considering the statement: \n"Home-schooling is better than traditional schooling." \nWhich of the following perspectives may disagree?': ['A student who enjoys socializing with classmates in a traditional school.', 'A teacher who believes they can provide better instruction than a parent.'],
        'Consider the issue of regulation of social media content (such as laws limiting what can be shared on social media). \nWhich perspective might support stricter regulations?': 'A government official concerned about fake news.'
    }

    # Complete dictionary of correct answers keyed by column index
    correct_answers_by_index = {
        16: 'School uniforms should be mandatory.',
        23: 'No',
        -1: '$0.05'
    }
        
    df['Pre-survey'] = 0
        
    for idx, column in enumerate(df.columns[16:]):
        correct_answer = None
        if column in correct_answers_by_name:
            correct_answer = correct_answers_by_name[column]
        elif idx + 16 in correct_answers_by_index:
            correct_answer = correct_answers_by_index[idx + 16]
        
        # Assign a score of 1 if the answer is correct, 0 otherwise
        if correct_answer is not None:
            df['Score'] = df[column].apply(lambda x: 1 if x == correct_answer else 0)
            
            # Add the score for this question to the total score
            df['Pre-survey'] += df['Score']
            
            # Drop the temporary Score column
            df.drop('Score', axis=1, inplace=True)
        
    return df[['Level', 'Major', 'Gender', 'Age', 'Parental education', 'English proficiency', 'Working students', 'Living with',
        'GPA', 'Pre-survey']]
    
    
def calculate_post_scores(df):
    # Dictionary of correct answers keyed by question (column name)
    correct_answers = {
        "Consider the statement: 'Vaccinations should be mandatory because they prevent serious diseases.' \nWhat is the main claim?": "Vaccinations should be mandatory.",
        "In the previous question statement, what is used as support for the claim?": "Vaccinations prevent serious diseases.",
        "A project your team is working on is over budget. \nWhat could be a potential first step to address this problem?": "Analyze the budget and spending to identify cost overruns.",
        "Continue thinking about the scenario from the previous question. \nLet's say that you you decided to analyze the budget. You found some unnecessary expenses. \nWhat could be your next step?": "Cut all the unnecessary expenses.",
        "Consider the claim: \n'Regular physical activity reduces the risk of chronic diseases.' \nWhich of the following would be the strongest evidence for this claim?": "A scientific study showing that physically active people have lower rates of chronic disease.",
        "Continue thinking about the scenario from the previous question.\nBased on your selected answer about the best evidence, how strongly does it support the claim (0-weak, 2-strong)?": "2",
        "Consider the argument: \n'Strawberries are fruits. All fruits grow on trees. Therefore, strawberries grow on trees.' \nWhat is the mistake in this argument?": "Both",
        "If an argument says: \n'If it's hot, then people swim. It's cold. Therefore, people don't swim.' \nIs the logic of this argument valid or not?": "No",
        "Considering the statement: \n'Online learning is more effective than traditional classroom learning.' \nWhich of the following perspectives may disagree?": "A student who learns better in interactive, social environments.",
        "Consider the topic of implementing stricter gun control laws.\nWhich perspective might oppose stricter regulations?": "A citizen concerned about personal safety and self-defense.",
        "Consider the problem: \n'A coffee and a muffin cost $6 in total. The coffee costs $5 more than the muffin. How much does the muffin cost?' \nWhat's your answer?": "$0.5"
    }

    # Initialize a new score column
    df['Post-survey'] = 0

    for question, correct_answer in correct_answers.items():
        # Check if the question is in the DataFrame
        if question in df.columns:
            # Assign a score of 1 if the answer is correct, 0 otherwise
            df['Score'] = df[question].apply(lambda x: 1 if str(x).strip() == correct_answer else 0)
            
            # Add the score for this question to the total score
            df['Post-survey'] += df['Score']
            
            # Drop the temporary Score column
            df.drop('Score', axis=1, inplace=True)

    return df[['Level', 'Major', 'Gender', 'Age', 'Parental education', 'English proficiency', 'Working students', 'Living with',
        'GPA', 'Post-survey']]

import numpy as np

def bootstrap_scores(original_scores, target_length):
    return np.random.choice(original_scores, size=target_length, replace=True)
 