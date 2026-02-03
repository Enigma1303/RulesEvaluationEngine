import logging

class result_generation:

    def result(self,failed_rules):
        logging.info("Generating final result based on failed rules")
        if not failed_rules:
            logging.info("All rules passed. Entity Approved.")
            return {
                "decision": "Approved"
            }
        else:
            logging.info(f"{len(failed_rules)} rules failed. Entity Rejected.")
            return {
                "decision": "Rejected",
                "failed_rules":failed_rules
            }
            