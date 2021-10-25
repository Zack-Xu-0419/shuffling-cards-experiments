# Specify Values
numberOfDecks = 4
numberOfCards = 12


# Initiate Cards - Deck with 'numberOfCards' Cards (Here we use numbers instead of card. At the end of the day, they are unique)
def InitiateCards(numberOfCards):
    result = []
    for i in range(numberOfCards):
        result.append(i+1)
    return result

# Function - disperseDeck - that categorize Cards into 'numberOfDecks' Number of decks (Array[] -> Array[Array[]])


def disperseDeck(cardsArray):
    result = []
    for i in range(numberOfDecks):
        thisDeck = []
        count = 1
        for j in cardsArray:
            if count % numberOfDecks == i:
                thisDeck.insert(0, j)
            count += 1
        result.append(thisDeck)
    # When doing modulo, the pile that should appear last would actually appear first since it's divisible, this code is to ensure that it runs
    finalResult = []
    for i in range(numberOfDecks-1):
        finalResult.append(result[i+1])
    finalResult.append(result[0])
    ###

    return finalResult

# Function that takes the Array of Array from disperseDeck and flatten them into a whole deck of cards (Array[Array[]] -> Array[])


def flatten(distributedDeck):
    result = []
    for i in distributedDeck:
        for j in i:
            result.append(j)
    return result


# Main loop that will go through the functions, count the amount of times it takes until the returned value matches the original one


originalCards = InitiateCards(numberOfCards)

cards = disperseDeck(originalCards)
print(cards)
cards = flatten(cards)
print(cards)

cards = disperseDeck(cards)
print(cards)
cards = flatten(cards)
print(cards)

count = 0

print(count)
