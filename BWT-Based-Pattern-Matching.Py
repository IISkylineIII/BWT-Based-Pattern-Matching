def build_bwt(text):
    text += '$'  # Ensure the text includes the '$'
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    sorted_rotations = sorted(rotations)
    bwt = ''.join(rotation[-1] for rotation in sorted_rotations)
    return bwt

def build_first_occurrence(bwt):
    sorted_bwt = ''.join(sorted(bwt))
    first_occurrence = {char: sorted_bwt.find(char) for char in set(bwt)}
    return first_occurrence

def build_checkpoints(bwt, interval):
    n = len(bwt)
    checkpoints = {c: [0] * ((n // interval) + 1) for c in set(bwt)}
    count = {c: 0 for c in set(bwt)}

    for i in range(n):
        if i % interval == 0:
            for c in checkpoints:
                checkpoints[c][i // interval] = count[c]
        count[bwt[i]] += 1

    return checkpoints, count

def count_symbol_up_to(bwt, checkpoints, count, index, symbol, interval):
    if index == -1:
        return 0
    checkpoint_idx = index // interval
    base_count = checkpoints[symbol][checkpoint_idx]
    extra_count = sum(1 for i in range(checkpoint_idx * interval, index + 1) if bwt[i] == symbol)
    return base_count + extra_count

def better_bw_matching(bwt, patterns, first_occurrence, checkpoints, count, interval):
    results = []

    for pattern in patterns:
        top = 0
        bottom = len(bwt) - 1
        i = len(pattern) - 1

        while top <= bottom:
            if i >= 0:
                symbol = pattern[i]
                i -= 1
                top_count = count_symbol_up_to(bwt, checkpoints, count, top - 1, symbol, interval)
                bottom_count = count_symbol_up_to(bwt, checkpoints, count, bottom, symbol, interval)
                if bottom_count > top_count:
                    top = first_occurrence[symbol] + top_count
                    bottom = first_occurrence[symbol] + bottom_count - 1
                else:
                    results.append([])
                    break
            else:
                match_positions = list(range(top, bottom + 1))
                results.append(match_positions)
                break

    return results

def find_pattern_positions(text, patterns, interval=100):
    bwt = build_bwt(text)
    first_occurrence = build_first_occurrence(bwt)
    checkpoints, count = build_checkpoints(bwt, interval)
    matches = better_bw_matching(bwt, patterns, first_occurrence, checkpoints, count, interval)

    # Translate BWT positions to original text positions
    lf_mapping = [0] * len(bwt)
    sorted_bwt = ''.join(sorted(bwt))
    char_count = {char: 0 for char in set(bwt)}

    for i, char in enumerate(bwt):
        lf_mapping[i] = sorted_bwt.find(char) + char_count[char]
        char_count[char] += 1

    results = {}
    for pattern, match_positions in zip(patterns, matches):
        original_positions = []
        for pos in match_positions:
            original_pos = pos
            for _ in range(len(bwt)):
                if bwt[original_pos] == '$':
                    break
                original_pos = lf_mapping[original_pos]
            original_positions.append(original_pos)
        results[pattern] = sorted(original_positions)
    return results

def main():

    text = "AATCGGGTTCAATCGGGGT"
    patterns = ["ATCG", "GGGT"]

    result = find_pattern_positions(text, patterns)
    for pattern in patterns:
        positions = ' '.join(map(str, result[pattern]))
        print(f"{pattern}: {positions}")

if __name__ == "__main__":
    main()
