"""
Topic: Longest Winning Streak

PROBLEM:
You are given a list representing the results of points
played in a tennis match.

"W" = Point won
"L" = Point lost

Write a function that returns the longest number of
consecutive points won.

Example:
Input:  ["W", "W", "L", "W", "W", "W", "L", "W"]
Output: 3

Rules:
- Return 0 if there are no wins.
- Return 0 if the list is empty.
- Do not use external libraries.
"""


def longest_streak(points):
    # TODO: Write your solution here
    pass


# ------------------------------
# TEST CASES
# ------------------------------

def run_tests():
    test_cases = [
        (["W", "W", "L", "W", "W", "W", "L", "W"], 3),
        (["W", "W", "W"], 3),
        (["L", "L", "L"], 0),
        ([], 0),
        (["W", "L", "W", "L"], 1),
        (["L", "W", "W", "L", "W", "W", "W"], 3),
    ]

    passed = 0

    for i, (points, expected) in enumerate(test_cases, 1):
        result = longest_streak(points)

        if result == expected:
            print(f"Test {i}: PASSED")
            passed += 1
        else:
            print(f"Test {i}: FAILED")
            print(f"  Input:    {points}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")

    print(f"\nResults: {passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()