import argparse

from app.commands.importar_candidatos import executar


def main():
    parser = argparse.ArgumentParser(
        description="Radar Político Paraná"
    )

    parser.add_argument(
        "comando",
        help="Comando a executar"
    )

    args = parser.parse_args()

    if args.comando == "importar-candidatos":
        executar()
    else:
        print("Comando desconhecido.")


if __name__ == "__main__":
    main()