from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    var_fulltext = request.GET['fulltext']  # Fazendo o pedido da variavel fulltext que recebe o texto na pagina HTML

    wordlist = var_fulltext.split()  # Toda vez que tiver um espaco em branco, contara como uma palavra diferente

    #wordcountdict = [{}] # Dicionario com todas as palavras
    wordcountdict = {

    }

    for word in wordlist:
        if word in wordcountdict:
            # increase
            wordcountdict[word] += 1

        else:
            # add to dictionary
            wordcountdict[word] = 1

    # sortedwords = sorted(wordcountdict.items(), key=operator.itemgetter(1), reverse=True)
    # Funcao faz com que a lista desapareca no HTML
    return render(request, 'count.html',
                  {'fulltext': var_fulltext,
                   'count': len(wordlist),
                   'wordcountdict': wordcountdict},)  # Toda vez que referenciarmos 'fulltext', ele levara a variavel do HTML


def about(request):
    return render(request, 'about.html')