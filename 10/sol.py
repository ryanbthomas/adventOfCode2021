import day10

data = day10.load_input("input")


print("Part 1:")
total_syntax_score = 0
autocomplete_scores = []
for r in data:
    (score, unused_tokens) = day10.score_syntax_errors(r)
    total_syntax_score += score
    if score == 0:
        autocomplete_scores.append(day10.score_autocomplete(unused_tokens))
        print("unmatched tokens: {} |-> {}".format(unused_tokens, autocomplete_scores[-1]))
    
print("Total score: {}".format(total_syntax_score))

print("Part 2:")
idx = len(autocomplete_scores) // 2
autocomplete_scores.sort()
print("Mid-point autocomplete: {}".format(autocomplete_scores[idx]))