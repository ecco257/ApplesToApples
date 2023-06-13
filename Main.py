from DataTypes import *
from pprint import pprint
import inquirer
import random
import os

def run() -> None:
    num_players = int(input('How many players are there? '))
    
    assert num_players >= 3

    players = [Player('', 0) for i in range(num_players)]

    for i, player in enumerate(players):
        player.name = input('Player ' + str(i+1) + ', Input name: ')

    os.system('cls' if os.name == 'nt' else 'clear')

    green_cards = [
        'awkward',
        'cowardly',
        'delightful',
        'boring',
        'absurd',
        'chunky',
        'dangerous',
        'busy',
        'crazed',
        'cuddly',
        'cute',
        'dainty',
        'dead',
        'cosmic',
        'appetizing',
        'creative',
        'deadly',
        'addictive',
        'adorable',
        'cold',
        'cranky',
        'bold',
        'brilliant',
        'calm',
        'delicate',
        'arrogant',
        'bright',
        'ancient',
        'casual',
        'charismatic',
        'comical',
        'cool',
        'annoying',
        'clean',
        'cosmopolitan',
        'cruel',
        'aged',
        'American',
        'animated',
        'awesome',
        'believable',
        'bogus',
        'classic',
        'crazy',
        'delicious',
        'corrupt',
        'charming',
        'cheesy',
        'chewy',
        'comfortable',
        'complicated',
        'confused',
        'courageous',
        'boisterous',
        'clueless',
        'colorful',
        'creepy',
        'disturbing',
        'dramatic',
        'exhausting',
        'hard-working',
        'healthy',
        'honorable',
        'innocent',
        'insulting',
        'naîve',
        'shallow',
        'silly',
        'smelly',
        'unbelievable',
        'explosive',
        'extreme',
        'glamorous',
        'rare',
        'repulsive',
        'risky',
        'spunky',
        'unnatural',
        'dignified',
        'eccentric',
        'fabulous',
        'foreign',
        'funky',
        'heartless',
        'hot',
        'inspirational',
        'legendary',
        'misunderstood',
        'nasty',
        'obnoxious',
        'painful',
        'primitive',
        'radical',
        'revolutionary',
        'scary',
        'sharp',
        'technological',
        'tough',
        'trustworthy',
        'unforgettable',
        'frazzled',
        'global',
        'intelligent',
        'loud',
        'pathetic',
        'rough',
        'smooth',
        'weird',
        'depressing',
        'European',
        'expensive',
        'principled',
        'relaxing',
        'sexy',
        'unscrupulous',
        'visionary',
        'woebegone',
        'exciting',
        'fancy',
        'flirtatious',
        'frivolous',
        'influential',
        'juicy',
        'natural',
        'stereotyped',
        'unusual',
        'virtuous',
        'desperate',
        'dysfunctional',
        'distinguished',
        'dreamy',
        'earthy',
        'filthy',
        'frightening',
        'furious',
        'idiotic',
        'scenic',
        'stunning',
        'sweet',
        'temperamental',
        'graceful',
        'horrifying',
        'insane',
        'manly',
        'mystical',
        'overwhelming',
        'popular',
        'refined',
        'rich',
        'senseless',
        'sensitive',
        'shocking',
        'spooky',
        'demanding',
        'emotional',
        'dirty',
        'elitist',
        'friendly',
        'glorious',
        'goody-goody',
        'important',
        'industrious',
        'melodramatic',
        'patriotic',
        'realistic',
        'responsible',
        'sappy',
        'shiny',
        'snappy',
        'spicy',
        'wild',
        'eternal',
        'fantastic',
        'feminine',
        'fuzzy',
        'ordinary',
        'peaceful',
        'radiant',
        'saintly',
        'speedy',
        'tame',
        'touchy-feely',
        'zany',
        'fragrant',
        'handsome',
        'funny',
        'irresistible',
        'luscious',
        'magical',
        'masculine',
        'miserable',
        'odd',
        'offensive',
        'playful',
        'puffy',
        'ridiculous',
        'spiritual',
        'sultry',
        'talented',
        'worldly',
        'intense',
        'meek',
        'outrageous',
        'pure',
        'shy',
        'soft',
        'hopeless',
        'neat',
        'neglected',
        'normal',
        'organic',
        'perfect',
        'philosophical',
        'phony',
        'smart',
        'timeless',
        'useless',
        'wicked',
        'dull',
        'harmful',
        'hilarious',
        'lovable',
        'lucky',
        'nerdy',
        'sensual',
        'swift',
        'unhealthy',
        'violent',
        'easy',
        'fake',
        'glitzy',
        'powerful',
        'quiet',
        'selfish',
        'witty',
        'exquisite',
        'fresh',
        'haunting',
        'hostile',
        'irritating',
        'lazy',
        'luxurious',
        'mischievous',
        'mysterious',
        'profound',
        'refreshing',
        'squeaky clean',
        'twisted',
        'unreal'
    ]

    random.shuffle(green_cards)

    judge = players[0]

    while True:
        responses = []
        if len(green_cards) == 0:
            print('All Green Cards finished. Final results:\n')
            for player in players:
                print(player)
            break
        green_card_this_round = green_cards.pop(0)
        for player in players:
            if player.name != judge.name:
                print('Green Card: ' + green_card_this_round + '\n')
                response = input(player.name + ', Type a Red Card to match this Green Card: ')
                while response == '' or response in responses:
                    if response == '':
                        response = input('response cannot be nothing')
                    else:
                        response = input('this response has already been used by another player before you')
                responses.append(tuple([response, player]))
                os.system('cls' if os.name == 'nt' else 'clear')

        options = [responses[i][0] for i in range(len(responses))]

        random.shuffle(options)

        questions = [
            inquirer.List(
                green_card_this_round,
                message=judge.name + ", which response best matches the green card, " + green_card_this_round + "?",
                choices=options,
            ),
        ]

        answer = inquirer.prompt(questions)

        for response in responses:
            if response[0] == answer[green_card_this_round]:
                response[1].points += 1
                judge = response[1]

        print('Round over. ' + judge.name + ' wins. Results:\n')

        for player in players:
            print(player)

        input('')
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    run()