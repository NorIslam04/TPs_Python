while True:
    word = input("Please enter a string: ")

    frame_width = 30

    # Calculate the left and right padding
    padding = (frame_width - len(word)) // 2

    # Print the frame
    print("*" * frame_width)
    print("*" + " " * padding + word + " " * padding + "*")
    print("*" * frame_width)