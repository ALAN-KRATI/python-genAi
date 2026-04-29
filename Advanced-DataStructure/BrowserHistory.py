back_stack = []
forward_stack = []


back_stack.append("A")
back_stack.append("B")
back_stack.append("C")


forward_stack.append(back_stack.pop())  # remove C

back_stack.append(forward_stack.pop())  # bring C back

print("Current Page:", back_stack[-1])