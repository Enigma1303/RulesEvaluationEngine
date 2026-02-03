import logging

logging.basicConfig( 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="rules_evaluation_engine.log",
    filemode="a"
) 
from rules_parser_and_validation import RulesParserAndValidation
from rules_evaluator import RulesEvaluator
from result_generation import result_generation    
def main():
    logging.info("Starting Rules Evaluation Engine")
    rules_parser = RulesParserAndValidation()
    rules=rules_parser.load_rules('D:\\RulesEvaluationEngine\\rules.json')
    
    validator=RulesEvaluator(rules)
    failedrules=validator.load_entity('D:\\RulesEvaluationEngine\\entity.json')
    
    generator=result_generation()
    FINAL_RESULT=generator.result(failedrules)
    
    logging.info("Rules Evaluation Completed")
    print(FINAL_RESULT)
    
if __name__ == "__main__":
    main()
    
    
    