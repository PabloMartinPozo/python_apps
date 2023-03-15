import PySimpleGUI as sg
player_one = "X"
player_two = "O"
game_end = False
current_player = player_one
deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]
winner_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
layout = [[sg.Button("", key="-0-", size=(7, 3)),
           sg.Button("", key="-1-", size=(7, 3)),
           sg.Button("", key="-2-", size=(7, 3))],
          [sg.Button("", key="-3-", size=(7, 3)),
           sg.Button("", key="-4-", size=(7, 3)),
           sg.Button("", key="-5-", size=(7, 3))],
          [sg.Button("", key="-6-", size=(7, 3)),
           sg.Button("", key="-7-", size=(7, 3)),
           sg.Button("", key="-8-", size=(7, 3))],
          [sg.Button("CERRAR", key="-OK-")]]
window = sg.Window("Demo", layout)
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == "-OK-":
        exit()
    if window.Element(event).ButtonText == "" and not game_end:
        index = int(event.replace("-", ""))
        deck[index] = current_player
        print(deck)
        window.Element(event).Update(text=current_player)
        for winner_play in winner_plays:
            if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
                if deck[winner_play[0]] == player_one:
                    print("EL JUGADOR 1 HA GANADO")
                    game_end = True
                else:
                    print("EL JUGADOR 2 HA GANADO")
                    game_end = True
        if 0 not in deck:
            print("EMPATE")
            exit()
        if current_player == player_one:
            current_player = player_two
        else:
            current_player = player_one