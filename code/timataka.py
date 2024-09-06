import requests
import pandas as pd
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Vinna með úrslit af tímataka.net.')
    parser.add_argument('--url', help='Slóð að vefsíðu með úrslitum.')
    parser.add_argument('--output', required=True,
                        help='Slóð að útgangsskrá til að vista niðurstöðurnar (CSV format).')
    parser.add_argument('--debug', action='store_true',
                        help='Vistar html í skrá til að skoða.')
    return parser.parse_args()


def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Tókst ekki að sækja gögn af {url}")
        return None


def parse_html(html):
    # Hér þarf að útfæra reglulega segð til að vinna úr niðurstöðum, ekki er leyfilegt að nota
    # pakka eins og BeautifulSoup til að leysa verkefnið.
    raise NotImplementedError("Eftir að útfæra reglulega segð sem vinnur úr HTML gögnum.")


def skrifa_nidurstodur(data, output_file):
    """
    Skrifar niðurstöður í úttaksskrá.
    :param data:        (list) Listi af línum
    :param output_file: (str) Slóð að úttaksskrá
    :return:            None
    """
    if not data:
        print("Engar niðurstöður til að skrifa.")
        return

    df = pd.DataFrame(data)
    df.to_csv(output_file, sep=',', index=False)
    print(f"Niðurstöður vistaðar í '{output_file}'.")


def main():
    args = parse_arguments()

    if not args.output.endswith('.csv'):
        print(f"Inntaksskráin {args.output} þarf að vera csv skrá.")
        return

    if not 'timataka.net' in args.url:
        # TODO uppfærið if-skilyrðið til að nota reglulega segð sem passar að URL sé frá
        #  timataka.net og sýnir úrslit, t.d.
        #  https://timataka.net/jokulsarhlaup2024/urslit/?race=2&cat=m
        #  https://www.timataka.net/snaefellsjokulshlaupid2014/urslit/?race=1&cat=m&age=0039
        #  en ekki
        #  https://www.timataka.net/snaefellsjokulshlaupid2014/urslit/?race=1
        print("Slóðin er ekki frá timataka.net")
        return

    html = fetch_html(args.url)
    if not html:
        raise Exception("Ekki tókst að sækja HTML gögn, athugið URL.")

    if args.debug:
        html_file = args.output.replace('.csv', '.html')
        with open(html_file, 'w') as file:
            file.write(html)
        print(f"HTML fyrir {args.url} vistað í {html_file}")

    results = parse_html(html)
    skrifa_nidurstodur(results, args.output)


if __name__ == "__main__":
    main()
