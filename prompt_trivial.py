def queryZephyr(prompt):
    return prompt  + " What happens next?"

if __name__ == '__main__':
    time_to_stop = False

    while not time_to_stop:
        # Taking input from the user
        prompt = input("Enter the prompt: ")
 
        # Output
        if prompt.strip().lower() == 'exit':
            time_to_stop = True
        else:
            print(queryZephyr(prompt))
    