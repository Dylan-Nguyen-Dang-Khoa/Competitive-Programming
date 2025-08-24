n, q = map(int, input().split())
pages = []
questions = []
for i in range(n):
    pages.append(int(input()))
for i in range(q):
    questions.append(int(input()))
for page in questions:
    print(pages[page - 1])