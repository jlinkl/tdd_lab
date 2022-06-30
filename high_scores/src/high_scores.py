def latest(scores):
    latest_score = scores[-1]
    return latest_score

def personal_best(scores):
    top_score = 0
    for score in scores:
        if score > top_score:
            top_score = score
    return top_score



def personal_top_three(scores):
    best_to_last = sorted(scores)
    if len(best_to_last) < 3:
        return best_to_last[::-1]
    else:
        return  [best_to_last[-1], best_to_last[-2], best_to_last[-3]]

def highest_to_lowest(scores):
    high_to_low = sorted(scores)
    return high_to_low[::-1]