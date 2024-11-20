def hello(name, lang):
    greetings = {
        "English": "Hello", 
        "Spanish": "Hola", 
        "German": "Hallo", 
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == "__main__":
    import argparse as ap

    parser = ap.ArgumentParser()
    parser.add_argument("-n", "--name", metavar="name", required=True)
    parser.add_argument("-l", "--lang", metavar="language", required=True)

    args = parser.parse_args()
    hello(args.name, args.lang)
