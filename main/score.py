
def calculate_score(request_dict):
    question = {}
    answer = {}
    for key, value in request_dict.iteritems():
        if key.isdigit():
            key_to_string = str(key)
            convert_key = str(filter(str.isdigit, key_to_string))
            answer[convert_key] = value[-1]
        if key.startswith('group'):
            key_to_string = str(key)
            convert_key = str(filter(str.isdigit, key_to_string))
            question[convert_key] = value[-1]
    temp_array_value = []
    for key in answer:
        if key.isdigit():
            temp_array_value.append(int(key))

    min_val = min(temp_array_value)

    current_answer_count = 0
    for dict_index in xrange(len(question)):
        key_index = dict_index + min_val
        if question.get(str(key_index)) == answer.get(str(key_index)):
            current_answer_count += 1
    user_score = round((current_answer_count / float(len(question)) * 100))

    return user_score
