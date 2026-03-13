from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"{result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if isinstance(data, (int)):
            return f"Processed 1 numeric value, sum={data}, avg={data}"
        return f"Processed {len(data)} numeric values, sum={sum(data)}, avg={(sum(data) / len(data)):.1f}"
    
    def validate(self, data: Any) -> bool:
        if isinstance(data, List):
            for number in data:
                if not isinstance(number, (int)):
                    return False
            return True
        elif isinstance(data, (int)):
            return True
        else:
            return False
        
    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        index = 0
        w_count = 0
        w_found = False
        while index < len(data):
            if data[index] != ' ' and data[index] != '  ':
                w_found = True
            else:
                w_found = False
                w_count += 1
            index += 1
        if w_found:
            w_count += 1
        return f"Processed text: {index} characters, {w_count} words"
    
    def validate(self, data: Any) -> bool:
        if isinstance(data, (str)):
            if data.find("ERROR: ", 0, 7) == 0 or data.find("INFO: ", 0, 6) == 0:
                return False
            return True
        else:
            return False
    
    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if data.find("ERROR: ", 0, 7) == 0:
            return f"[ALERT] ERROR level detected: {data[7:]}"
        elif data.find("INFO: ", 0, 6) == 0:
            return f"[INFO] INFO level detected: {data[6:]}"
        return f"[MESSAGE] DEFAULT level detected: {data[9:]}"
    
    def validate(self, data: Any) -> bool:
        if isinstance(data, (str)):
            if data.find("ERROR: ", 0, 6) or data.find("INFO: ", 0, 5):
                return True
            return False
        else:
            return False
    
    def format_output(self, result: str) -> str:
        return super().format_output(result)
    

def data_picker(data: Any, announce: bool = False) -> int:
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    if num_proc.validate(data):
        if announce:
            print("Validation: Numeric data verified")
        return 0
    elif text_proc.validate(data):
        if announce:
            print("Validation: Text data verified")
        return 1
    elif log_proc.validate(data):
        if announce:
            print("Validation: Log data verified")
        return 2
    else:
        print("Validation failed: Unknown data found")
        return -1
    

def stream_processor(data: Any, announce: bool = False) -> str:
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    alert = False
    if announce:
        print(f"Processing data {data}")
        alert = True
    d_type = data_picker(data, alert)
    if d_type == 0:
        return num_proc.format_output(num_proc.process(data))
    elif d_type == 1:
        return text_proc.format_output(text_proc.process(data))
    elif d_type == 2:
        return log_proc.format_output(log_proc.process(data))
    else:
        return f"[ERROR]: Unknown data type: {data}"



if __name__ == "__main__":
    num_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"
    data_types = [[1, 2, 3], "Hello world!", "INFO: System ready"]
    index = int(0)
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    print("Initializing Numeric Processor...")
    print(f"Output: {stream_processor(num_data, True)}")
    print()
    print("Initializing Text Processor...")
    print(f"Output: {stream_processor(text_data, True)}")
    print()
    print("Initializing Log Processor...")
    print(f"Output: {stream_processor(log_data, True)}")
    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    for data in data_types:
        print(f"Result {(index + 1)}: {stream_processor(data)}")
        index += 1
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")
