"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1,2,3,4,5]],
            "answer": 55
        },
        {
            "input": [[0,1,2]],
            "answer": 5
        },
        {
            "input": [[]],
            "answer": 0
        }
    ],
    "Extra": [
        {
            "input": [[3]],
            "answer": 9
        },
    ]
}
