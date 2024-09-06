import argparse


def parse_arguments():
    """
    Lesa inn argument frá skipanalínu
    :return: (ArgumentParser) parser með argumentunum
    """

    parser = argparse.ArgumentParser(description='Leita að kennitölum einstaklinga eða fyrirtækja.')
    parser.add_argument('--file', required=True,
                        help='Slóð að inntaksskrá með kennitölum.')
    parser.add_argument('--einstaklingar', action='store_true',
                        help='Leita að kennitölum einstaklinga.')
    parser.add_argument('--fyrirtaeki', action='store_true',
                        help='Leita að kennitölum fyrirtækja.')
    return parser.parse_args()


def lesa_skra(file_path):
    """
    Lesa inntaksskrá og skila lista af línum
    :param file_path: (str) Slóð að skrá
    :return:          (list) Listi af línum
    """

    with open(file_path, 'r') as file:
        return file.readlines()


def prenta_nidurstodur(kennitolur):
    """
    Prentar út niðurstöður í console
    :param kennitolur: (list) Listi af kennitölum
    :return:           None
    """

    if kennitolur:
        print("Fundnar kennitölur:")
        for kt in kennitolur:
            print(kt)
    else:
        print("Engar kennitölur fundust.")


def finna_kennitolur(text, leit_af_einstaklingum, leit_af_fyrirtaekjum):
    """
    Leita að kennitölum í texta með reglulegum segðum
    :param text:                    (list) Listi af línum
    :param leit_af_einstaklingum:   (bool) Leita að kennitölum einstaklinga
    :param leit_af_fyrirtaekjum:    (bool) Leita að kennitölum fyrirtækja
    :return:                        (list) Listi af kennitölum
    """

    kennitolur = []

    if leit_af_einstaklingum:
        # Regluleg segð fyrir kennitölur einstaklinga
        raise NotImplementedError("Fall sem leitar að kt einstaklinga hefur enn ekki verið útfært.")

    if leit_af_fyrirtaekjum:
        # Regluleg segð fyrir kennitölur fyrirtækja
        raise NotImplementedError("Fall sem leitar að kt fyrirtækja hefur enn ekki verið útfært.")

    return kennitolur


def main():
    """
    Keyrslufall sem les inn skrá, leitar að kennitölum og prentar niðurstöður.
    :return: None
    """

    args = parse_arguments()

    # Athuga hvort valkostir séu valdir; ef ekkert er valið, hætta og sýna villu
    if not args.einstaklingar and not args.fyrirtaeki:
        print("Þú verður að velja annað hvort --einstaklingar eða --fyrirtaeki eða bæði.")
        return

    text = lesa_skra(args.file)
    kennitolur = finna_kennitolur(text, args.einstaklingar, args.fyrirtaeki)

    prenta_nidurstodur(kennitolur)


if __name__ == "__main__":
    main()
