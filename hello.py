import queue
q= queue.PriorityQueue()

q.put((1,'A'))
q.put((3,'B'))
q.put((2,'C'))

for i in range(q.qsize()):
    print(q.get())

print("순서: git status")
print("순서: git add .")
print("순서: git status")
print("순서: git commit -m 올리는 이름")
print("순서: git branch")
print("순서: git push -u origin master")