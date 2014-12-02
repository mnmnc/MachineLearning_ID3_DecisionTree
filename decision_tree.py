import pprint
import math
import copy


data = [
	{"AURA": 0, "TEMP": 0, "WILG": 0, "WIND": 1, "PLAY": 0},  # 1
	{"AURA": 0, "TEMP": 0, "WILG": 0, "WIND": 0, "PLAY": 0},  # 2
	{"AURA": 1, "TEMP": 0, "WILG": 0, "WIND": 1, "PLAY": 1},  # 3
	{"AURA": 2, "TEMP": 1, "WILG": 0, "WIND": 1, "PLAY": 1},  # 4
	{"AURA": 2, "TEMP": 2, "WILG": 1, "WIND": 1, "PLAY": 1},  # 5
	{"AURA": 2, "TEMP": 2, "WILG": 1, "WIND": 0, "PLAY": 0},  # 6
	{"AURA": 1, "TEMP": 2, "WILG": 1, "WIND": 0, "PLAY": 1},  # 7
	{"AURA": 0, "TEMP": 1, "WILG": 0, "WIND": 1, "PLAY": 0},  # 8
	{"AURA": 0, "TEMP": 2, "WILG": 1, "WIND": 1, "PLAY": 1},  # 9
	{"AURA": 2, "TEMP": 1, "WILG": 1, "WIND": 1, "PLAY": 1},  # 10
	{"AURA": 0, "TEMP": 1, "WILG": 1, "WIND": 0, "PLAY": 1},  # 11
	{"AURA": 1, "TEMP": 1, "WILG": 0, "WIND": 0, "PLAY": 1},  # 12
	{"AURA": 1, "TEMP": 0, "WILG": 1, "WIND": 1, "PLAY": 1},  # 13
	{"AURA": 2, "TEMP": 1, "WILG": 0, "WIND": 0, "PLAY": 0}   # 14
]


def count_values_for_attribute(local_data, attr, attr_value):
	counter = 0
	for element in local_data:
		if element[attr] == attr_value:
			counter += 1
	#print("Counted", counter, attr_value, "values for", attr, "attribute.")
	return counter


def get_number_of_unique_values(local_data, attr):
	values = []
	for element in local_data:
		if element[attr] not in values:
			values.extend([element[attr]])
	return len(values)


def get_unique_values(local_data, attr):
	values = []
	for element in local_data:
		if element[attr] not in values:
			values.extend([element[attr]])
	return values


def get_data_entropy(local_data, decision_attribute):
	values_array = []
	result = 0
	data_set_size = len(local_data)
	values = get_unique_values(local_data, decision_attribute)
	for value in values:
		number = count_values_for_attribute(local_data, decision_attribute, value)
		values_array.append({value:number})

	for i in range(len(values_array)):
		val = 0
		for key in (values_array[i]).keys():
			v = values_array[i][key]
			val = int(v)
			result += -1 * (val/data_set_size) * math.log2(val/data_set_size)
	return result


def get_attribute_value_entropy(local_data, decision_attr, attr, attr_value, decision_positive_value, decision_negative_value):
	positive_values = 0
	negative_values = 0
	for element in local_data:
		if element[attr] == attr_value and element[decision_attr] == decision_positive_value:
			positive_values += 1
		if element[attr] == attr_value and element[decision_attr] == decision_negative_value:
			negative_values += 1
	if negative_values == 0 or positive_values == 0:
		return 0
	else:
		return -1 * (negative_values / (negative_values + positive_values)) \
			  * math.log2(negative_values / (negative_values + positive_values)) \
			  - (positive_values / (negative_values + positive_values)) \
			  * math.log2(positive_values / (negative_values + positive_values))


def get_number_of_value_occurance(local_data, attr, attr_value):
	counter = 0
	for element in local_data:
		if element[attr] == attr_value:
			counter += 1
	return counter


def get_attribute_gain(local_data, decision_attr, attr, decision_positive_value, decision_negative_value):
	attribute_gain = get_data_entropy(local_data, decision_attr)
	attribute_values = get_unique_values(local_data, attr)
	for value in attribute_values:
		value_entropy = get_attribute_value_entropy(local_data, decision_attr, attr, value, decision_positive_value, decision_negative_value)
		attribute_gain  -= (get_number_of_value_occurance(local_data,attr,value) / len(local_data) * value_entropy)
	return attribute_gain


def get_best_node(local_data, decision_attr, decision_positive_value, decision_negative_value):
	global nodes_processed
	attributes = list(local_data[0].keys())
	best_attribute = None
	highest_value = -1
	for attribute in attributes:
		if attribute != decision_attr and attribute not in nodes_processed:
			attribute_gain = get_attribute_gain(local_data, decision_attr, attribute, 1, 0)
			if attribute_gain > highest_value:
				highest_value = attribute_gain
				best_attribute = attribute
	return best_attribute


def build_new_data_set(local_data, root_attribute, root_attribute_value):
	data_set = []
	for element in local_data:
		if element[root_attribute] == root_attribute_value:
			data_set.append(copy.deepcopy(element))
	for element in data_set:
		del(element[root_attribute])
	return data_set


def check_for_uniform_decision(local_data, decision_attribute, root_attribute, root_attribute_value):
	check = 0
	value = None
	for element in local_data:
		if value == None:
			value = element[decision_attribute]
		else:
			if value != element[decision_attribute]:
				check += 1
	if check == 0:
		return 0
	else:
		return 1


def build_tree(local_data, decision_attribute, decision_positive_value, decision_negative_value):
	global nodes_processed
	root = None
	if len(nodes_processed) < 1:
		root = get_main_root(local_data, decision_attribute,decision_positive_value,decision_negative_value)
		nodes_processed.append(root)
	else:
		root_attribute_values = get_unique_values(data,root)


def get_main_root(local_data, decision_attribute, decision_positive_value, decision_negative_value):
	node_attribute = get_best_node(local_data, decision_attribute,decision_positive_value,decision_negative_value)
	pass


def main():
	global nodes_processed, result
	nodes_processed = []
	result = []

	node_attribute = get_best_node(data, "PLAY",1,0)
	nodes_processed.append(node_attribute)
	node_attribute_values = get_unique_values(data,node_attribute)
	for value in node_attribute_values:
		local_data_set = build_new_data_set(data, node_attribute, value)
		uniform = check_for_uniform_decision(local_data_set,"PLAY", node_attribute, value)
		if uniform != 0:
			next_node_attribute = get_best_node(local_data_set, "PLAY",1,0)
			

if __name__ == "__main__":
	main()
