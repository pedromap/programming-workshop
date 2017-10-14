def take_survey():
    """ Function: ask a single user some questions. """

    # Note: literal text in your program is always surrounded either by ' or "
    name = input("What's your name?")

    # ... ask more questions, check answers

    # Return results as dictionary
    return {
        'name': name,
        # ...
    }


def ask_continue():
    """ Ask whether we want to continue. """
    yesno = input("Do you want to enter more? (Y/N)")

    # Below you see 4 spaces before the statements *within* the if condition.
    # This is to discriminate to computers and humans alike that these
    # statements belong together with either the if, if else (elif) or else.

    if yesno == 'Y':
        # True is a 'boolean' type, equivalent to a 0 and 1 in binary
        # See: boolean logic
        return True
    elif yesno == 'N':
        return False
    else:
        # Invalid responses go here
        print("I did not understand your answer, please try again.")

        # Recursion; the function calls itself(!) which causes the yesno
        # question to be asked again and again
        return ask_continue()


# Now actually run our magnificient functions!
go_on = True
answers = []

while go_on:
    # Take survey, add results to (initially empty) list, creating a list of
    # dictionaries.
    answer = take_survey()
    answers.append(answer)

    # Update go_on with result of asking whether to continue
    go_on = ask_continue()


### Now to go the other way!
### Note: for now, there is no validation on filter_data!

def filter_data(field, answers):
    """
    Take field name, ask for value equivalence, return filtered results.
    """
    # .format(argument1, argument2) replaces {} and {}, in order with arguments
    question = 'Requested value for field {}: '.format(field)

    valid_answer = False

    while not valid_answer:
        value = input(question)

        if field == 'color':
            if value in ['green', 'blue']:
                valid_answer = True
        elif field == '...':
            # Validate more fields
            pass
        else:
            print('Invalid answer! Try again')

    # Construct new values
    new_answers = []
    for answer in answers:
        if answer[field] == value:
            # Copy data
            new_answers.append(answer)
        else:
            print('Discarding {}', answer['name'])

# Iterate over fields; take next one out of fields, assign it to field
fields = ['gender', 'color']  # etc
for field in fields:
    print('Data collected:', answers)
    answers = filter_data(field, answers)
