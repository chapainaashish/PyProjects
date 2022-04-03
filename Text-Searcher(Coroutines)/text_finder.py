# Author: Aashish Sharma
# Github: https://github.com/aasis2520c

# exercise to search text in .txt file and retrieve it using coroutines

def text_searcher():
    import time
    time.sleep(3)
    with open("/home/aashish/Documents/python_journey/python_exercise/problems.txt", "r") as story:
        story_content = story.read()

    while True:
        txt = (yield)

        if txt in story_content:
            print("Successfully Found! ")
            continue

        else:
            print("Not Found")
            continue


while True:
    print("Running.......")
    search = text_searcher()
    next(search)

    user_text = str(input("Enter a text: "))
    search.send(user_text)
    user_text2 = str(input("Enter a text: "))
    search.send(user_text2)
    search.close()
