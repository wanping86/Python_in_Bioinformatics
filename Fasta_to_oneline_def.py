def deal_with_fasta(filename):
	
	seq_dict={}
	
	f=open(filename,'r')
	
	seq = f.read()
	
	seq_split_list = [x for x in seq.split('>') if x]
	
	for i in seq_split_list:
		lin_list=i.split('\n')
		seq_dict[lin_list[0]]=''
		for j in lin_list[1:]:
			seq_dict[lin_list[0]]=seq_dict[lin_list[0]]+j
	
	return seq_dict