import numpy as np
def calculate(key):
	result={}
	if isinstance(key, list):
		if len(key)== 9:
			x = np.matrix(np.array(key).reshape((3, 3)))
			mean_axis1=x.mean(0)
			mean_axis2=x.mean(1)
			flatted=x.flatten()
			media=np.mean(flatted)
			result.update({'mean': [mean_axis1.tolist()[0],mean_axis2.tolist()[0],media]})
			varianc_axis1=x.var(0)
			varianc_axis2=x.var(1)
			variance=np.var(flatted)
			result.update({'variance':[varianc_axis1.tolist()[0],varianc_axis2.tolist()[0],variance]})
			stand_axis1=x.std(0)
			stand_axis2=x.std(1)
			stand=np.std(flatted)
			result.update({'standard deviation':[stand_axis1.tolist()[0],stand_axis2.tolist()[0],stand]})
			max_axis1=x.max(0)
			max_axis2=x.max(1)
			maxi=np.max(flatted)
			result.update({'max':[max_axis1.tolist()[0],max_axis2.tolist()[0],maxi]})
			min_axis1=x.min(0)
			min_axis2=x.min(1)
			mini=np.min(flatted)
			result.update({'max':[min_axis1.tolist()[0],min_axis2.tolist()[0],mini]})
			sum_axis1=x.sum(0)
			sum_axis2=x.sum(1)
			suma=np.sum(flatted)
			result.update({'sum':[sum_axis1.tolist()[0],sum_axis2.tolist()[0],suma]})
			print(result)
		else:
		    print("List must contain nine numbers.")	

	else:
	    print("Must insert a list data type as a parameter")