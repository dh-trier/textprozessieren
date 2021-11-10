"""
Skript, das Unterschiede zwischen zwei Texten findet.
Verwendet wdiff.

Dokumentation: https://www.gnu.org/software/wdiff/manual/wdiff.html
Um herauszufinden, wie man wdiff auf der Kommandozeile startet.

Uses subprocess to call wdiff from the command line.
https://docs.python.org/3/library/subprocess.html

You need to have wdiff installed.
Based on the input texts split into sentences,
wdiff first aligns the text, identifying insertions and deletions. 
It then identifies each location of difference between two aligned sentences.


Documentation
- https://www.gnu.org/software/wdiff/manual/wdiff.html#wdiff-invocation
- Basic call: wdiff option old_file new_file > output
- Optionen: "--ignore-case", "--statistics", "--avoid-wraps"



"""


# === Imports ===

import subprocess


# === Functions ===

def call_wdiff(file1, file2, diffedfile):
    """Executes the wdiff algorithm via a subprocess command."""
    command = "wdiff --avoid-wraps " + file1 + " "\
              + file2 + " > " + diffedfile
    print(command)
    subprocess.run(command, shell=True)
    print("Done.")



# === Main ===

def main():
    file1 = "text1.txt"
    file2 = "text2.txt"
    diffedfile = "diffedTEST.txt"
    call_wdiff(file1, file2, diffedfile)

if __name__ == "__main__":
    main()



