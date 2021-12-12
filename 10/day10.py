def load_input(file_name):
    f = open(file_name, "r")
    out = []

    line = f.readline()
    while line:
        out.append(list(line[0:-1]))
        line = f.readline()

    return out

def score_syntax_errors(line):
    stack = []
    opens = ['(', '[', '{', '<']
    closes = [')', ']', '}', '>']
    scores = [3, 57, 1197, 25137]

    for token in line:
        if token in opens:
            stack.append(token)
        if token in closes:
            if token != closes[opens.index(stack.pop())]:
                return scores[closes.index(token)], None
    return 0, stack

def score_autocomplete(tokens):

    points = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4
    }
    # reverse order
    total_score = 0
    while tokens:
        total_score *= 5
        total_score += points[tokens.pop()]

    return total_score

if __name__ == "__main__":

    data = load_input("example")

    print("Example Data:")
    total_syntax_score = 0
    autocomplete_scores = []

    for r in data:
        (score, unused_tokens) = score_syntax_errors(r)
        #print("{} |-> {}".format(r, score))
        total_syntax_score += score
        if score == 0:
            autocomplete_scores.append(score_autocomplete(unused_tokens))
            print("unmatched tokens: {} |-> {}".format(unused_tokens, autocomplete_scores[-1]))

    print("Total score: {}".format(total_syntax_score))
    idx = len(autocomplete_scores) // 2
    autocomplete_scores.sort()
    print("Mid-point autocomplete: {}".format(autocomplete_scores[idx]))


