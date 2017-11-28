#Written by David Philiphose
#4/14/16
class Translator:
    def __init__(self,document):
        self._document=file(document)
        line=self._document.readline()
        self._dictionary={}
        while line:
            linelist=line.split()
            self._dictionary[linelist[0]]=linelist[1]
            line=self._document.readline()
        self._document.close()
    def translate(self,sentence):
        self._sentence=sentence
        sentencelist=self._sentence.split()
        for word in sentencelist:
            wordlist=sentencelist[word].split()
            for letter in wordlist:
                print self._dictionary[letter] 
    def __str__(self):
        for letter in self._dictionary:
            print "The letter:",letter,"in Morse code is:",self._dictionary[letter]
if __name__=='__main__':
    q=raw_input('What is the name of the file for morse code?')
    t=Translator(q)
    print t
    sen=raw_input("Enter a sentence in all capital letters:")
    t.translate(sen)
       
