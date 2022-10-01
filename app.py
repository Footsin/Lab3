import argparse
from cipher import get_caesar

def main():
    parser = argparse.ArgumentParser(description='Шифрование и расшифровка текста шифром Цезаря.')

    parser.add_argument('-s', '--step', type=int, help="сдвиг букв по шифру")
    parser.add_argument('-t', '--text', type=str, help="сам текст")
    parser.add_argument('-i', '--input', type=str, help="Откуда брать текст")
    parser.add_argument('-o', '--output', type=str, help="Куда отправлять результат")

    args = parser.parse_args()

    if not args.step:
        args.step = int(input("Введите шаг >> "))

    if not args.text:
        if args.input:
            with open(args.input, "r", encoding="utf-8") as file:
                args.text = file.read()

        else: 
            args.text = input("Введите текст >> ")

    result = get_caesar(args.text, args.step)

    # Печать результата в консоль/файл
    if args.output:
        with open(args.output, "w+", encoding="utf-8") as file:
            file.write(result)
            print("Ваш результат записан в указанном файле:", args.output)

    else:
        print("Ваш результат:", result)

if __name__ == "__main__":
    main()
