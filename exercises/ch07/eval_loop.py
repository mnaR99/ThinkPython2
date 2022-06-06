
def eval_loop():
    result = ""
    while True:
        command = input()
        if command == "done":
            return result
            break
        result = eval(command)
        print(result)


eval_loop()
