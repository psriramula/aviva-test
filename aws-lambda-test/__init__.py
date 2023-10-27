
import json
from schemas import INPUT_SCHEMA
from aws_lambda_powertools.utilities.validation import validate
from CloudWatchLambdaFunction import lambda_handler




def load_sample_event_from_file(test_event_file_name: str) ->  dict:
    """
    Loads and validate test events from the file system
    """
    event_file_name = f"{test_event_file_name}.json"
    with open(event_file_name, "r", encoding='UTF-8') as file_handle:
        event = json.load(file_handle)
        validate(event=event, schema=INPUT_SCHEMA)
        return event

def main():
    print("starting test")
    test_event =  load_sample_event_from_file("sampleEvent1")
    print ("test event ")
    print(test_event)
    res = lambda_handler(test_event, context=None)
    print(res)




if __name__ == "__main__":
    main()


