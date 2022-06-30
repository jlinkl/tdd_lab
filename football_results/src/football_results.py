def get_result(final_score):
    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"
    elif final_score["home_score"] < final_score["away_score"]:
        return "Away win"
    else:
        return "Draw"

def get_results(final_scores):
    results = []
    for score in final_scores:
        results.append(get_result(score))
    return results
    # (You could try and use a list comprehension for this)