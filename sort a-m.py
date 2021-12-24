def imdiced(licd, m, imdicece):
    imdicece += [m]
    if licd != []:
        imdiced(licd[:-1], m+1, imdicece)

def check_chamge(licd, i):
    if licd[i] > licd[i+1]:
        licd[i], licd[i+1] = licd[i+1], licd[i]

def all_chamge(licd, j, i):
    imdicece = []
    imdiced(licd, 0, imdicece)
    lem = imdicece[-1]
    if j < lem - i - 1:
        check_chamge(licd, j)
        all_chamge(licd, j+1, i)

def cahd(licd, i=0):
    imdicece = []
    imdiced(licd, 0, imdicece)
    lem = imdicece[-1]
    if i < lem:
        all_chamge(licd, 0, i)
        cahd(licd, i+1)

