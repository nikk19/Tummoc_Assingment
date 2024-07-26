def print_candidates(candidates):
    for i, candidate in enumerate(candidates, start=1):
        print(f"{i}. {candidate}")

def vote(candidates, votes, num):
    if 1 <= num <= len(candidates):
        candidate = candidates[num - 1]
        votes[candidate] += 1
        return True
    return False

def print_winner(votes):
    max_votes = max(votes.values(), default=0)
    winners = [candidate for candidate, vote_count in votes.items() if vote_count == max_votes]
    for winner in sorted(winners):
        print(winner)

candidates = ['Alice', 'Bob', 'Charlie']
votes = {candidate: 0 for candidate in candidates}

num_people = 5

for _ in range(num_people):
    print("\nCandidates:")
    print_candidates(candidates)
    try:
        num = int(input("Enter the number of the candidate you want to vote for (or 0 to finish): "))
        if num == 0:
            break
        if vote(candidates, votes, num):
            print("Vote recorded.")
        else:
            print("Invalid candidate number.")
    except ValueError:
        print("Please enter a valid number.")

print("\nElection Results:")
print_winner(votes)
