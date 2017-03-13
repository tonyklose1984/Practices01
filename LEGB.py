# x = 1
# def foo():
#     x = 2
#     def innerfoo():
#         #x = 3
#         print 'locals',x
#     innerfoo()
#     print 'enclosing function locals',x
#
# foo()
# print 'global',x

# a = 1
# def foo():
#     a = 2
#     print a
# print a
# foo()
#
# a = 1
#
# def foo():
#     a = 2
#     def bar():
#         print a
#     return bar
#
# func = foo()
# func()
# print a

# import Queue
# q = Queue.Queue()
#
# for i in range(8):
#     q.put(i)
#
# while not q.empty():
#     print q.get()

