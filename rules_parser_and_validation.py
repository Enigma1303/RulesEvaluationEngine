import json 
from operator_mapping import OPERATOR_MAP
class RulesParserAndValidation:
    
    def load_rules(self, filepath):
        try:
            print("Loading rules from file...")
            file = open(filepath, 'r')
            rules = file.read()
            # As these rules are a string we cannot iterate or use them need to convert to python object first  
            rulesobject = json.loads(rules)
            print(rulesobject)
            ## print(type(rulesobject[1])) so its a list of dictionaries
            if not rules:
                raise ValueError("The rules file is empty.")
            return self.validate_rules(rulesobject)   
        except FileNotFoundError:
            raise FileNotFoundError("The specified rules file was not found.")
        except IsADirectoryError:
            raise IsADirectoryError("The specified path is a directory, not a file.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the rules file: {e}")     
        finally:
            file.close()      
    
    def validate_rules(self, rulesobject):     
        print("Validation of rules starts now...")
        valid_rules=[]
        
        for index,rule in enumerate(rulesobject):
            if self.is_valid(rule):
                valid_rules.append(rule)
            else:
                print(f" Rule {index} positon object {rule} was found invalid and will be skipped")
           
        return valid_rules 
    
    def is_valid(self, rule):
        #we need to think of cases which makes a rule invalid, maybe some field is missing, operator is not in our map
        
        if not {"field","operator","value"}.issubset(rule):
            print(f"Missing some keys in Rule {rule}")
            return False
        
        if rule["operator"] not in OPERATOR_MAP:
            print(f"Invalid Operator in Rule {rule}")
            return False  
        
        return True    
        

       