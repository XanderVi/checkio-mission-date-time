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
            "input": "01.01.2000 00:00",
            "answer": "1 January 2000 year 0 hours 0 minutes"
        },
        {
            "input": "09.05.1945 06:07",
            "answer": "9 May 1945 year 6 hours 7 minutes"
        }
    ],
    "Extra": [
        {
            "input": "20.11.1990 03:55",
            "answer": "20 November 1990 year 3 hours 55 minutes"
        },
        {
            "input": "09.07.1995 16:01",
            "answer": "9 July 1995 year 16 hours 1 minute"
        },
	{
            "input": "11.04.1812 01:01",
            "answer": "11 April 1812 year 1 hour 1 minute"
        }
    ]
}
