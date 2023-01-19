# slightly smiling unicode is U0001F642
# slightly frowning unicode is U0001F641
# print emoji as "\####"
def convert(text):
    return(text.replace(":)", "\U0001F642").replace(":(", "\U0001F641"))

def main(response):
    print(response)

feeling = input("How are you feeling? ",)
main(convert(feeling))
