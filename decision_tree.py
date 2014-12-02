import pprint
import math
import copy
from colorama import Fore

# AURA	0 Sunny | 1 Cloud | 2 Rain
# TEMP	0 High  | 1 Medium | 2 Low
# WILG  0 High  | 1 Normal
# WIND  0 High  | 1 Low
# PLAY  0 No	| 1 Yes

mapping = {
	"AURA": ["Sunny", "Cloudy", "Raining"],
	"TEMP": ["High", "Medium", "Low"],
	"WILG": ["High", "Normal"],
	"WIND": ["High", "Low"],
	"PLAY": ["No", "Yes"]
}

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
	{"AURA": 2, "TEMP": 1, "WILG": 0, "WIND": 0, "PLAY": 0}  # 14
]


def count_values_for_attribute(local_data, attr, attr_value):
	"""	Given data set, attribute and attribute value checks
		for number of value occurances for given attribute """
	counter = 0
	for element in local_data:
		if element[attr] == attr_value:
			counter += 1
	if debug == 1:
		print(debug_prefix + "Counted", counter, attr_value, "values for", attr, "attribute." + debug_postfix)
	return counter


def get_number_of_unique_values(local_data, attr):
	"""	Given data set and attribute, checks
		for number of values that the attribute can take """
	values = []
	for element in local_data:
		if element[attr] not in values:
			values.extend([element[attr]])
	return len(values)


def get_unique_values(local_data, attr):
	"""	Given data set and attribute, returns
		unique values that the attribute takes """
	values = []
	for element in local_data:
		if element[attr] not in values:
			values.extend([element[attr]])
	return values


def get_data_entropy(local_data, decision_attribute):
	""" Calculates entropy for given attribute and data set. """
	values_array = []
	result = 0
	data_set_size = len(local_data)
	values = get_unique_values(local_data, decision_attribute)
	for value in values:
		number = count_values_for_attribute(local_data, decision_attribute, value)
		values_array.append({value: number})

	for i in range(len(values_array)):
		for key in (values_array[i]).keys():
			v = values_array[i][key]
			val = int(v)
			result += -1 * (val / data_set_size) * math.log2(val / data_set_size)
	return result


def get_attribute_value_entropy(local_data, decision_attr, attr, attr_value, decision_positive_value,
								decision_negative_value):
	""" Calculates entropy for particular value of given attribute. """
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


def get_number_of_value_occurrence(local_data, attr, attr_value):
	counter = 0
	for element in local_data:
		if element[attr] == attr_value:
			counter += 1
	return counter


def get_attribute_gain(local_data, decision_attr, attr, decision_positive_value, decision_negative_value):
	# Attribute gain initialized with entropy level of all data.
	# Gain(S, Attribute) =
	# Entropy(S) -
	# (Attr_pos/(Attr_pos+Attr_neg))log2(Attr_pos/(Attr_pos+Attr_neg)) -
	# (Attr_neg/(Attr_pos+Attr_neg))log2(Attr_neg/(Attr_pos+Attr_neg))

	attribute_gain = get_data_entropy(local_data, decision_attr)
	if debug == 1:
		print(debug_prefix + "Full data entropy:", str(attribute_gain) + debug_postfix)
	attribute_values = get_unique_values(local_data, attr)
	for value in attribute_values:
		if debug == 1:
			print(debug_prefix + "Calculating for", attr, " for value", str(value) + debug_postfix)
		value_entropy = get_attribute_value_entropy(local_data, decision_attr, attr, value, decision_positive_value,
													decision_negative_value)
		attribute_gain -= (get_number_of_value_occurrence(local_data, attr, value) / len(local_data) * value_entropy)
	if debug == 1:
		print(debug_prefix + "Gain for attribute", attr, "is", str(attribute_gain) + debug_postfix)
	return attribute_gain


def get_best_node(local_data, decision_attr, decision_positive_value, decision_negative_value):
	attributes = list(local_data[0].keys())
	best_attribute = None
	highest_value = -1
	for attribute in attributes:
		if attribute != decision_attr:
			attribute_gain = get_attribute_gain(local_data, decision_attr, attribute, decision_positive_value, decision_negative_value)
			if attribute_gain > highest_value:
				highest_value = attribute_gain
				best_attribute = attribute
	if debug == 1:
		print(debug_prefix + "Highest gain given by attribute:", best_attribute + debug_postfix)
	return best_attribute


def build_new_data_set(local_data, root_attribute, root_attribute_value):
	data_set = []
	for element in local_data:
		if element[root_attribute] == root_attribute_value:
			data_set.append(copy.deepcopy(element))
	for element in data_set:
		del (element[root_attribute])
	if debug == 1:
		(pprint.PrettyPrinter(indent=8)).pprint(data_set)
	return data_set


def check_for_uniform_decision(local_data, decision_attribute):
	check = 0
	value = None
	for element in local_data:
		if value is None:
			value = element[decision_attribute]
		else:
			if value != element[decision_attribute]:
				check += 1
	if check == 0:
		return 0
	else:
		return 1


def build_tree(local_data, current_root, decision_attribute, decision_positive_value, decision_negative_value, indent):
	if current_root is None:
		print(debug_prefix + "No root detected. Searching for first one." + debug_postfix)
		new_root = get_best_node(local_data, decision_attribute, decision_positive_value, decision_negative_value)
		print(debug_prefix + "New root found:", new_root + debug_postfix)
		indent = "\t"
		build_tree(local_data, new_root, decision_attribute, decision_positive_value, decision_negative_value, indent)
	else:
		if debug == 1:
			print(debug_prefix + "Getting unique values for ", current_root + debug_postfix)
		new_root_values = get_unique_values(local_data, current_root)
		indent += "\t"
		for value in new_root_values:
			print(indent + "Calculation for:", Fore.GREEN + current_root, "=", mapping[current_root][value] + Fore.RESET)

			new_data_set = build_new_data_set(local_data, current_root, value)
			uniform_decision = check_for_uniform_decision(new_data_set, decision_attribute)
			if uniform_decision == 0:
				print(indent + "\t\tDecision: ", Fore.YELLOW, decision_attribute, "=",	new_data_set[0][decision_attribute], Fore.RESET)
			else:
				next_root = get_best_node(new_data_set, decision_attribute, decision_positive_value, decision_negative_value)
				if debug == 1:
					print("\tFound new root:", next_root)
				build_tree(new_data_set, next_root, decision_attribute, decision_positive_value, decision_negative_value, indent)


def main():
	global debug, debug_prefix, debug_postfix
	debug = 1
	debug_prefix = "\t\t[DBG] " + Fore.BLUE
	debug_postfix = Fore.RESET
	build_tree(data, None, "PLAY", 1, 0, None)


if __name__ == "__main__":
	main()
