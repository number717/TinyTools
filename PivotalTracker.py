import requests
import xlrd
import xlwt
from xlutils.copy import copy

def main():
	queryState()
	#getState("138291147")

def queryState():
	rb = xlrd.open_workbook("stories.xlsx", on_demand=True)
	sr = rb.sheet_by_index(0)
	nrows = sr.nrows
	wb = copy(rb)
	sw = wb.get_sheet(0)
	for i in range(nrows):
		storyID = str(int(sr.cell(i,0).value))
		state = getState(storyID)
		print storyID + ' ' + state
		sw.write(i, 1, state)
	wb.save('Stories state.xls')

def getState(storyID):
	proID1 = '1573173'
	proID2 = '1573171'
	#storyID = '139339517'
	url = 'https://www.pivotaltracker.com/services/v5/projects/' + proID1 + '/stories/' + storyID
	headers = {'X-TrackerToken': '8cb0f4f9124ee6937b9e82a64e253995'}
	r = requests.get(url, headers=headers)
	if r.json().has_key('current_state'):
		state = r.json()['current_state']
	else:
		url = 'https://www.pivotaltracker.com/services/v5/projects/' + proID2 + '/stories/' + storyID
		r = requests.get(url, headers=headers)
		if r.json().has_key('current_state'):
			state = r.json()['current_state']
		else:
			state = ''
	return state



if __name__ == "__main__":
	main()