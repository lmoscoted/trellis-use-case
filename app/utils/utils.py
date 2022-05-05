
# Change this if a higher number need to be supported.
GREATER_THAN_TENS = {100: 'hundred ', 1000: 'thousand '} #,
                    # 1000000: 'million ', 1000000000: 'billion ', 10000000000000: 'trillion '}
MAX_NUMBER_SUPPORTED = 1000 * max([n for n in GREATER_THAN_TENS.keys()])

def number_to_english(num):

    under_twenty = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                    'eleven', 'twelve', 'thirdteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty',
            'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    # Base cases CORREGIR PARA CASOS CUANDO DA ZERO "one hundred zero thousand zero"
    if num < 20:
        return (under_twenty[int(num)])

    if num < 100:
        return tens[int(num)//10] + (' ' + under_twenty[int(num) % 10] if num % 10 else '')

    # getting the maximun ten multiple of the given  number.
    pivot = max([tens for tens in GREATER_THAN_TENS.keys() if int(num)//tens])

    # Recursion
    return number_to_english((int(num)/pivot)) + ' ' + GREATER_THAN_TENS[pivot] + number_to_english(int(num) % pivot)


def number_is_supported(num):
    if num >= MAX_NUMBER_SUPPORTED:
        return False
    return True
