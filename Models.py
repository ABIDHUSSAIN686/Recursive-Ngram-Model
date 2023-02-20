

# Recursive N-Gram

def readDataset():
# Dataset for designing model
  file = "/Dataset.txt"
  dataset = open(file, "r")
  return dataset

def generateCorpus(dataset ):
# Spliting the Dataset into words
  corpus=[]
  for sentence in dataset:
    corpus+=sentence.split()
  return corpus

def generateVocabulary( corpus ):
#Finding the unique words in the corpus 
  vocabulary = []
  data=""
  for word in corpus:
      data +=word+" "
      if word not in vocabulary:
          vocabulary.append(word)
  return vocabulary

def generateUnigramArray(corpus ):
#Designing the Uni-gram Array
  Unigram_Array={}
  for items in corpus:
    Unigram_Array[items] = corpus.count(items)
  return Unigram_Array


size=5
def recursivengram(n,ngram_Array,vocabulary,corpus):
  #Recursive Function for generating n-gram
  previousgram=ngram_Array
  ngram_Array={}
  ngram_Model={}
  for index1 in range(len(corpus)):
    sentence=""
    if index1 < len(corpus)-(n-1):
      for i in range(n-1):
        if(i==0 and index1 < len(corpus)-(n-1)):
          sentence+=corpus[index1]
        else:
          if index1 < len(corpus)-(n-1):
            sentence+=" "+corpus[index1+i]
      ngram_Array[sentence] = dict()
      ngram_Model[sentence] = dict()
      for index in range(len(vocabulary)):
        ngram_Array[sentence][vocabulary[index]]=0 

  searched_word=""
  searched_word1=""
  for index1 in range(len(corpus)):
    if index1 < len(corpus)-(n-1):
      sentence=""
      for i in range(n-1):
        if(i==0):
          sentence+=corpus[index1]
        else:
          if index1 < len(corpus)-(n-1):
            sentence+=" "+corpus[index1+i]
      
      for index in range(len(vocabulary)):
        searched_word=""
        for i in range(n-1):
          if(i==0):
            searched_word+=corpus[index1]
          elif i>0 and i<n: 
            if index1 < len(corpus)-(n-1):
              searched_word+=" "+corpus[index1+i]
        
        searched_word+=" "+ vocabulary[index] 
        count =0
        for words in range(len(corpus)):
          searched_word1=""
          for i in range(n):
            if i==0:
              searched_word1+=corpus[words+i]
            elif words < len(corpus)-(n-1):
              searched_word1+=" "+corpus[words+i]
          if searched_word==searched_word1:
            count+=1
          
          ngram_Array[sentence][vocabulary[index]]=count
          word1=""
          word2=""  
          temp=[]
          temp=sentence.split()      
          for i in range(len(temp)):
            if i==0:
              word1+=temp[i]
            if i>0 and i<len(temp)-1:
              word1+=" "+temp[i]
            if i==len(temp)-1:
              word2=temp[i]
          if (n>2):
            ngram_Model[sentence][vocabulary[index]]=(count+1)/(previousgram[word1][word2]+len(vocabulary))  
  if size==n:
    return ngram_Array,previousgram,ngram_Model

  return recursivengram(n+1,ngram_Array,vocabulary,corpus)



def main():
  dataset =readDataset()
  corpus = generateCorpus(dataset)
  vocabulary = generateVocabulary(corpus)
  Unigram_Array = generateUnigramArray(corpus)
  Bigram=dict()
  ngram_Array,previousgram,ngram_Model=recursivengram(2,Bigram,vocabulary,corpus)

  # Printing all Models
  print('Unigram Array')
  print(Unigram_Array)
  print('previousgram Array')
  print(previousgram)
  print('ngram Array')
  print(ngram_Array)
  print('ngram Model')
  print(ngram_Model)


if __name__ == "__main__":
    main()