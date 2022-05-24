import sys
import json

def school_out(file):
	with open(file,'r') as f:
		schedule = json.load(f)

	timeline = {}
	reponse = 0
	for course in schedule:
		mn = int(course['start'].replace(':',''))
		mx = int(course['end'].replace(':',''))
		if (mn not in timeline):
			timeline[mn] = []
		if (mx not in timeline):
			timeline[mx] = []
	for i,y in timeline.items():
		for course in schedule:
			mn = int(course['start'].replace(':',''))
			mx = int(course['end'].replace(':',''))
			if (i >= mn and i <mx):
				y.append(str(i)+'-'+str(mn)+'-'+str(mx))
				reponse = len(y)  if len(y) > reponse  else reponse
	return reponse

def main():

    print(school_out(sys.argv[1]))


if __name__ == '__main__':
    main()
