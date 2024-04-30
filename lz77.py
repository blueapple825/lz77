def compression(text):
    pass

if __name__ == "__main__":
    inputText = input("text: ").encode("utf-8")
    result=compression(inputText)

    print("결과: ", result)
    print("압축률: ", len(result) / len(inputText))
