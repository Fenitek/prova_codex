#!/usr/bin/env python3

"""Semplice gioco di escape room testuale."""

def main():
    print("Benvenuto nell'Escape Room Testuale!")
    print("Digita un comando (guarda, apri cassetto, prendi chiave, usa chiave, apri porta, esci)")

    drawer_open = False
    door_open = False
    inventory = set()

    while not door_open:
        command = input('> ').strip().lower()

        if command == 'guarda':
            description = []
            if not drawer_open:
                description.append("C'e' un tavolo con un cassetto chiuso.")
            else:
                if 'chiave' in inventory:
                    description.append("Il cassetto del tavolo e' aperto, ma e' vuoto.")
                else:
                    description.append("Nel cassetto aperto vedi una chiave.")
            description.append("La porta e' chiusa.")
            print(' '.join(description))

        elif command == 'apri cassetto':
            if drawer_open:
                print("Il cassetto e' gia' aperto.")
            else:
                drawer_open = True
                print('Hai aperto il cassetto.')

        elif command == 'prendi chiave':
            if not drawer_open:
                print('Non vedi nessuna chiave qui.')
            elif 'chiave' in inventory:
                print("Hai gia' preso la chiave.")
            else:
                inventory.add('chiave')
                print('Hai preso la chiave.')

        elif command in ('usa chiave', 'apri porta'):
            if 'chiave' not in inventory:
                print('Non hai la chiave per aprire la porta.')
            else:
                door_open = True
                print('Hai usato la chiave per aprire la porta. Sei uscito!')

        elif command in ('esci', 'quit'):
            print('Hai abbandonato il gioco.')
            return
        else:
            print('Comando non valido.')

    print('Complimenti, hai completato il gioco!')


if __name__ == '__main__':
    main()
