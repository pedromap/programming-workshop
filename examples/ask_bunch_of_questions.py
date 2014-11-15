# Ask a bunch of questions in a loop

# Create answers as an empty list
answers = []

# Ask three questions
questions_total = 3
question_count = 0

while question_count < questions_total:
    answer = raw_input(question_count)
    answers.append(answer)

    question_count = question_count + 1

# 'Iterate' over the list answers
# Get next value from answers list in answer
for answer in answers:
    print answer
