import xml.etree.ElementTree as ET
import os


def get_test_statuses():
	test_statuses = []
	with open('result.txt','r') as file:
		for line in file:
			status = line.strip()
			test_statuses.append(status)
	return test_statuses


def get_all_coverage_filenames(rootdir="."):
	filenames = []
	for filename in os.listdir(rootdir):
		if filename.endswith(".xml"):
			file_path = os.path.join(rootdir,filename)
			filenames.append(file_path)
	return sorted(filenames)


def tarantula():
	test_statuses = get_test_statuses()
	coverage_filenames = get_all_coverage_filenames()
	#=====complete the code below======#

	#Read each XML file, go through each line of code, find out which lines get executed and which do not.
	#Store this information somewhere
	line_coverage_hits= {}
	line_status_count = {}
	for filename in coverage_filenames:
		tree = ET.parse(filename)
		root = tree.getroot()
		for line in root.find('.//lines'):
			line_number = line.attrib['number']
			hits = int(line.attrib['hits'])
			# print(line_number, hits)
			# key = f"line {line_number}"
			# if key in coverage_hits:
			if line_number in line_coverage_hits:
				line_coverage_hits[line_number].append(hits)
			else:
				line_coverage_hits[line_number] = [hits]
	# print(f"line_coverage_hits = {line_coverage_hits}")

	for key, values in line_coverage_hits.items():
		passed_count = 0
		failed_count = 0
		for i in range(len(values)):
			if test_statuses[i] == 'passed' and values[i] == 1:
				passed_count += 1
			if test_statuses[i] == 'failed' and values[i] == 1:
				failed_count += 1
		line_status_count[key] = {'passed': passed_count, 'failed': failed_count}
	# print(f"line_status_count = {line_status_count}")
		
	#For each line of code, calculate its suspiciousness value across all test cases
	suspiciousness_dict = {}
	total_passed = test_statuses.count('passed')
	total_failed = test_statuses.count('failed')
	for key, values in line_status_count.items():
		failed = values['failed']
		passed = values['passed']
		# (failed / total_failed) / ((failed / total_failed) + (passed / total_passed))
		passRatio = passed / total_passed
		failedRatio = failed / total_failed
		divider = passRatio + failedRatio
		
		if divider == 0:
			suspiciousness = 0
		else:
			suspiciousness = failedRatio / divider

		suspiciousness_dict[f"line {key}"] = suspiciousness
	# print(f"suspiciousness_dict = {suspiciousness_dict}")
	

	#print top 5 most suspiciousness lines.
	sorted_suspiciousness_dict = dict(sorted(suspiciousness_dict.items(), key=lambda item: item[1], reverse=True)[:5])

	for i in sorted_suspiciousness_dict:
		print(f"{i} suspiciousness : {sorted_suspiciousness_dict[i]:.2f}")
	# print(f"sorted_suspiciousness_dict = {sorted_suspiciousness_dict}")
	

	



	#====== end of your code =====

if __name__ == "__main__":
    tarantula()
