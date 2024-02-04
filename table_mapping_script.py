

first_break = r'{"rules":[{"rule-type":"selection","rule-id":"'

second_break = r'","rule-name":"589500340","object-locator":{"schema-name":"DMS","table-name":"'

third_break = r'"},"rule-action":"include","filters":[],"parallel-load":null,"isAutoSegmentationChecked":false},'

#above can be used if they also want to generate table selection rules, below is just the generic definitions for the transformation

transform_only_break = r'{"rule-type":"transformation","rule-id":"'

third_point_five_break = r'","rule-name":"2","rule-action":"add-column","rule-target":"column","object-locator":{"schema-name":"DMS","table-name":"'

fourth_break = r'"},"value":"adjusted_'

fifth_break = r'","expression":"CASE WHEN $'

sixth_break = r'=\'\' THEN \'null\' ELSE $'

seventh_break = r' END","data-type":{"type":"string","length":50}}'


print('what is the table name?')

table_name = input()


print('what are the column names?')

col_names = input()



#print(type(col_names))

parse_cols = col_names.split(", ")

#print(parse_cols)

#print(type(parse_cols))

num_col = 0

for col_name_parse_iter in parse_cols:
    #print(col_name_parse_iter)
    num_col = num_col + 1

#
    
print(num_col)



number = 1234
other_num = 6789

for col_name_parse_iter in parse_cols:
    
    table_mapping_rule =  transform_only_break + str(other_num) + third_point_five_break + table_name + fourth_break + col_name_parse_iter + fifth_break + col_name_parse_iter + sixth_break + col_name_parse_iter + seventh_break

    parsed_table_mapping = table_mapping_rule.replace("\\", '')
    #result = string.replace("\\","")

    number = number + 1

    print(parsed_table_mapping)




