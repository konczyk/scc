# SCC 

Compute strongly connected components of a directed graph using Kosaraju's
algorithm.

## Sample client

Client options:

    $ ./client.py -h

Compute strongly connected components in a graph read from the standard input:

    $ ./client.py graph.txt

    {7, 8, 9, 10, 11, 12}
    {2, 4, 5}
    {3, 6}
    {1}

Compute strongly connected components in a graph read from the standard input
and display two biggest ones:

    $ ./client.py -t 2 graph.txt

    {7, 8, 9, 10, 11, 12}
    {2, 4, 5}

Compute strongly connected components in a graph read from the standard input
but display their sizes only:

    $ ./client.py -s graph.txt

    6
    3
    2
    1

Compute strongly connected components in a graph read from the standard input
and display sizes of the two biggest ones:

    $ ./client.py -s -t 2 graph.txt

    6
    3

