# Specify Values
numberOfDecks = 13
numberOfCards = 52


# Initiate Cards - Deck with 'numberOfCards' Cards (Here we use numbers instead of card. At the end of the day, they are unique)
def InitiateCards(numberOfCards):
    result = []
    for i in range(numberOfCards):
        result.append(i+1)
    return result

# Function - disperseDeck - that categorize Cards into 'numberOfDecks' Number of decks (Array[] -> Array[Array[]])


def disperseDeck(cardsArray, nDecks):
    result = []
    for i in range(nDecks):
        thisDeck = []
        count = 1
        for j in cardsArray:
            if count % nDecks == i:
                thisDeck.insert(0, j)
            count += 1
        result.append(thisDeck)
    # When doing modulo, the pile that should appear last would actually appear first since it's divisible, this code is to ensure that it runs
    finalResult = []
    for i in range(nDecks-1):
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

def calcNShuffle(n, d):
    originalCards = InitiateCards(n)

    shuffleNCount = 2
    cards = disperseDeck(originalCards, nDecks=d)
    cards = flatten(cards)

    while originalCards != cards:
        cards = disperseDeck(cards, nDecks=d)
        cards = flatten(cards)
        shuffleNCount += 1
    return shuffleNCount


result = []


for i in range(100):
    oneRow = []
    for j in range(100):
        oneRow.append(calcNShuffle(i+1, j+1))
    result.append(oneRow)

print(result)
