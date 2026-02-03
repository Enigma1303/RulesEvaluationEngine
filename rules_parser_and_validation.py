import logging
import json 
from operator_mapping import OPERATOR_MAP
class RulesParserAndValidation:
    
    def load_rules(self, filepath):
        try:
            logging.info(f"Loading files from path...{filepath}")
            file = open(filepath, 'r')
            rules = file.read()
            # As these rules are a string we cannot iterate or use them need to convert to python object first  
            rulesobject = json.loads(rules)
            logging.info(f"Rules loaded successfully.{rulesobject}")
            ## print(type(rulesobject[1])) so its a list of dictionaries
            if not rules:
                logging.error("The rules file is empty.")
                raise ValueError("The rules file is empty.") 
            
            logging.info("Sending loaded rules for validation.")    
            return self.validate_rules(rulesobject)  
         
        except FileNotFoundError:
            logging.error("The specified rules file was not found.")
            raise FileNotFoundError("The specified rules file was not found.")
        except IsADirectoryError:
            logging.error("The specified path is a directory, not a file.")
            raise IsADirectoryError("The specified path is a directory, not a file.")
        except Exception as e:
            logging.error(f"An error occurred while reading the rules file: {e}")
            raise Exception(f"An error occurred while reading the rules file: {e}")     
        finally:
            if file:
                logging.info("Closing the rules file.")
                file.close()      
    
    def validate_rules(self, rulesobject):     
        logging.info("Validating loaded rules...")
        valid_rules=[]
        
        for index,rule in enumerate(rulesobject):
            if self.is_valid(rule):
                valid_rules.append(rule)
            else:
                logging.warning(f" Rule {index} position object {rule} was found invalid and will be skipped")
                print(f" Rule {index} positon object {rule} was found invalid and will be skipped")
           
        return valid_rules 
    
    def is_valid(self, rule):
        #we need to think of cases which makes a rule invalid, maybe some field is missing, operator is not in our map
        if not isinstance(rule, dict):
            logging.warning(f"Rule {rule} is not a valid dictionary.")
            return False
        
        if not {"field","operator","value"}.issubset(rule):
            logging.warning(f"Rule {rule} is missing required keys.")
            return False
        
        if rule["operator"] not in OPERATOR_MAP:
            logging.warning(f"Operator {rule['operator']} is not supported.")
            return False  
        
        return True    
        

       