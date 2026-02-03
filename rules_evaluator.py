import json 
from operator_mapping import OPERATOR_MAP
import logging
class RulesEvaluator:
    
   def __init__(self, rules):
        self.rules = rules
        logging.info(f"RulesEvaluator initialized with {len(rules)} rules.")
        
   def load_entity(self,filepath):
       try:
           logging.info(f"Loading entity from file... {filepath}")
           file = open(filepath, 'r')
           entity = file.read()
           entityobject = json.loads(entity)
           print(entityobject)
           if not entityobject:
               logging.error("The entity file is empty.")
               raise ValueError("The entity file is empty.")
           
           logging.info("Entity loaded successfully.")
           return self.evaluate_rules(self.rules,entityobject) 
         
       except FileNotFoundError:
           logging.error("The specified entity file was not found.")
           raise FileNotFoundError("The specified entity file was not found.")
               
       except IsADirectoryError:
           logging.error("The specified path is a directory, not a file.")
           raise IsADirectoryError("The specified path is a directory, not a file.")
       
       except json.JSONDecodeError:
           logging.error("The entity file contains invalid JSON.")
           raise json.JSONDecodeError("The entity file contains invalid JSON.")
       
       except Exception as e:
           logging.error(f"An error occurred while reading the entity file: {e}")
           raise Exception(f"An error occurred while reading the entity file: {e}")  
          
       finally:
           if file:
              logging.info("Closing the entity file.") 
              file.close()

   def evaluate_rules(self, rules, entity):
         print("Evaluation of rules starts now...")
         #storing failed rules as they matter...
         failed_rules = []
         for rule in rules:
             field=rule["field"]
             operator=rule["operator"]
             value=rule["value"]
             
             #getting value of that field in entity and function to be used
             if field not in entity:
                 print(f" field {field} is missing in the entity {entity}")
                 failed_rules.append(rule)
                 #making sure the code continues
                 continue
                  
             valueinentity=entity[field]
             operatorfunction=OPERATOR_MAP[operator]  
             
             
             try:
                 if operatorfunction(valueinentity,value):
                    print(f"So {field} passed the rule {rule}")
                 else:
                    print(f"So {field} failed the rule {rule}")
                    failed_rules.append(rule)   
             except Exception as e:
                    print(f"An error occurred while evaluating the rule {rule} on field {field}: {e}")
                    failed_rules.append(rule)
                    
         return failed_rules                
          
    