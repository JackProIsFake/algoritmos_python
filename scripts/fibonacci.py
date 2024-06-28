# Retorna os X primeiros números da sequência
def fibonacci(qtt:int):
    sequence = [0,1]

    i = 2
    
    while i < 10:
        sequence.append(sequence[i-1] + sequence[i-2])
        i +=1
    
    return sequence
