<<<<<<< HEAD
import sys

fl=sys.argv[1]
text=" "
with open(fl,'r') as f:
	fl=f.readlines()	
def clean(text):
    text = text.lower() ## lowercase
    text = ''.join([char for char in text if char in 'abcdefghijklmnopqrstuvwxyz ']) ## remove punctuations etc.
    text = ' '.join(text.split())## remove multiple spaces
    return 
    
def entropy(prob_dict):
    return sum([-v*math.log2(v) for _,v in prob_dict.items()])

def entropy_from_iter(text):
    freq = Counter(text)
    total = len(text)
    prob = {k:v/total for k,v in freq.items()}
    return entropy(prob)

def create_n_grams(text,n=2):
    ngrams = []
    l = len(text)
    for i in range(len(text)-n-1):
        ngrams.append(text[i:i+n])
    return ngrams


for n in range(4):
    if n==0:
        print(f'{n}-gram: = ', math.log2(27))
    elif n==1:
        print(f'{n}-gram: = ', entropy_from_string(text))
    else:
        ngram  = create_n_grams(text,n)
        prevgram = create_n_grams(text,n-1)
        print(f'{n}-gram:   {entropy_from_string(ngram)} - { entropy_from_string(prevgram)} = ', entropy_from_string(ngram) - entropy_from_string(prevgram) )
=======
import torch 

#encoding
def encoding(list_of_string,pad_token_id=0):
	max_length=max([len(string) for string in list_of_string])
	
	#create empty tensors
	attentions_masks=torch.zeros((len(list_of_string),max_length), dtype=torch.long))
	input_ids=torch.full((len(list_of_strings),max_length),pad_token_id,dtype=torch.long)
	for idx, string in enumerate(list_of_strings):
		if not isinstance((string,bytes):
			string=str.encode(string)
		input_ids[idx,:len(strings)]=1
	
	return input_ids,attention_masks


#Decodeing
def decode(output_ids):
	decode_outputs=[]
	for output_ids in output_ids.tolist():
		# transform id back to char IDs <  2 are simply transformed to ""
		decoded_outputs.append("".join([chr(x-2)if x>1 else "" for x in output_ids]))
	return decoded_outputs

def entropy(pro_dicts):
	 return sum([-v*math.log2(v) for _,v in prob_dict.items()])

def entropy_from_iter(text):
	freq =counter(text)
	total=len(text)
	prob={k:v/total for k,v in freq.items()}
	return entropy(prob)
>>>>>>> e08cec0180894817278b4f0772bb804280565488
