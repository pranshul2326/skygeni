#write a function or class that return path of the data files.
def get_data_file_path(file_type):
    paths = {
        "finanical_info": "data_files/finanical_information.csv",
        "client_info": "data_files/industry_client_details.csv",
        "payment_info": "data_files/payment_information.csv",
        "subscription_info": "data_files/subscription_information.csv",
    }
    return paths.get(file_type, "Invalid file type")
