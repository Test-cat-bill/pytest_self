def a_new_decorator(a,b):
    print("inner_before")
    def inner(a_func):
        print(f"inner {a}")
        print(f"inner {b}")
        print("warp_before")
        def wrapTheFunction():
            print(a)
            print(b)
            print("I am doing some boring work before executing a_func()")

            a_func()

            print("I am doing some boring work after executing a_func()")
        print("warp_last")
        return wrapTheFunction
    print("inner_last")
    return inner

@a_new_decorator(a=2,b=3)
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


a_function_requiring_decoration()
# outputs: "I am the function which needs some decoration to remove my foul smell"

# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# now a_function_requiring_decoration is wrapped by wrapTheFunction()



# a_function_requiring_decoration()
# outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()