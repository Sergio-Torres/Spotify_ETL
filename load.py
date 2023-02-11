import extract
import transform
from sqlalchemy import create_engine 


if __name__ == "__main__":
    data = extract.extract_data()    
    data_ordered = transform.transform(data)
    validated_df = transform.data_quality(data_ordered)


