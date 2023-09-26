
def teamFormation(score, team_size, k):
    sum_scores = 0

    for _ in range(team_size):
        length_scores = len(score)
        if k*2 >= length_scores:
            employees_to_check = score
            max_value = max(employees_to_check)  # optimize
            index = employees_to_check.index(max_value)
            sum_scores += score.pop(index)
        else:
            employees_to_check = score[0:k] + score[length_scores - k:]
            max_value = max(employees_to_check)
            index = employees_to_check.index(max_value)

            if index > k:
                index_inverse = len(employees_to_check) - index
                sum_scores += score.pop(-index_inverse)
            else:
                sum_scores += score.pop(index)

    return sum_scores


def teamFormationChatGpt(score, team_size, k):
    sum_scores = 0

    while team_size > 0 and score:
        if k * 2 >= len(score):
            max_value_index = score.index(max(score))
        else:
            left_half = score[:k]
            right_half = score[-k:]
            combined_half = left_half + right_half
            max_value_index = combined_half.index(max(combined_half))

            if max_value_index >= k:
                max_value_index = score.index(combined_half[max_value_index])

        sum_scores += score.pop(max_value_index)
        team_size -= 1

    return sum_scores


if __name__ == '__main__':
    team_size = 3
    score = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k = 4

    print(teamFormationChatGpt(score, team_size, k))

